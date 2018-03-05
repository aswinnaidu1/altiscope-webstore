import dynamodb_service
from termcolor import cprint

class usercart:
    
    def __init__(self,conx,dydbtable):
        self.items = []
        self.id = 0
        self.conx = conx
        self.dydbproducts = dydbtable

    def get_cartid_from_carttable(self,user_name):
        with self.conx as cursor:
            # cursor = self.conx.cursor()
            check_saved_cart = "select max(cartid) from cart where username = %(usrnm)s and ordered = 0"
            cursor.execute(check_saved_cart,{'usrnm':user_name})
            self.id = cursor.fetchone()[0]
            cursor.close()
            return self.id

    
    def initialize_cart(self,username):
        self.user = username
        cartid = self.get_cartid_from_carttable(self.user)
        if cartid:
            self.cartid = cartid
            self.retrieve_saved_items()
            # self.list_saved_from_dynamodb()
        else:
            sql_create_cart = "insert into cart values(current_timestamp,%s,NULL,0)"
            with self.conx as cursor:
                cursor.execute(sql_create_cart,(username))
                self.conx.commit()
                cursor.close()
                self.cartid = self.get_cartid_from_carttable(self.user)
                self.saveditems = ()
    
    def add_item_to_cart(self,productid):
        self.items.append(productid)
        print ('Product %d added to cart') %productid

    def itemcount(self):
        return len(self.items)
        
    def list_items(self):
        items = self.items
        cprint ('products in the cart','red','on_white')
        for item in items:
            print ('function not in use %s') %item
        return items
        
    def retrieve_saved_items(self):
        with self.conx as cursor:
            savedcart_items = "select ci.sku from cartitems ci join cart c on c.cartid = ci.cartid where c.ordered = 0 and c.username = %(usrnm)s"
            itemcount = cursor.execute(savedcart_items,{'usrnm':self.user})
            if itemcount:
                items = cursor.fetchall()
                self.saveditems = items
                cprint ('products in the cart','red','on_white')
                for item in items:
                    dynamodb_service.get_item_from_dynamodb(item[0])
            else:
                self.saveditems = ()
            cursor.close()
        
        
            # print 'Pulling description from NoSQL for product %d' %item[0]
        # return items
        
        
    def delete_cart(self):
        with self.conx as cursor:
            delete_from_cart = "delete from cart where cartid = %d" %self.id
            cursor.execute(delete_from_cart)
            self.conx.commit()
            cursor.close()
        
    def put_items_in_cartitems(self):
        with self.conx as cursor:
            for item in self.items:
                sql = "insert into cartitems values(%d,%d)" %(self.id,item)
                cursor.execute(sql)
            cursor.close()
        self.conx.commit()
        
    def list_saved_from_dynamodb(self):
        for i in self.items:
            response = self.dydbproducts.get_item(IndexName='SKU-index',Key={'SKU': i})
            print(response[u'Items'])
            
        
        
        