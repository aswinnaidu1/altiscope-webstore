# from __future__ import print_function # Python 2/3 compatibility
from boto3.dynamodb.conditions import Key, Attr
import sys
import cart
import boto3
import dynamodb_service
from termcolor import cprint

# print('1')
def authenticate_user(conx,userid):
    with conx as cursor:
        # cursor = conx.cursor()
        sql = "select * from users where username = %(name)s"
        cursor.execute(sql,{'name':userid})
        cursor.fetchall()
        row_count = cursor.rowcount
        cursor.close()
    if row_count > 0:
        return True
        
# print('2')        
def go_shopping(conx,crt):
    # category = raw_input("What are you looking for? 1) book 2) shoes 3) laptop ")
    category = get_categories()
    # get_from_dynamodb(category)
    changecategory = 0
    while not changecategory:
        dynamodb_service.get_from_dynamodb(category)
        cprint ('\n 1) Enter sku (# in Decimal(sku) ) of the product you want to add to cart \n 2) Or enter the number 0 to checkout \n 3) Or enter 1 to change product category \n 4) Or enter -1 to save cart and logout: \n','red','on_white')
        productid = int(input(""))
        # productid = input("\nenter sku (# in Decimal(sku) ) of the product you want to add to cart\n \n Enter the number 0 to checkout \n enter 1 to changecategory \n enter -1 to save cart and logout: \n")
        if productid == 0:
            checkout_cart(crt)
            sys.exit("Thank you")
        elif productid == -1:
            cprint ('Cart saved','red','on_white') 
            crt.put_items_in_cartitems()
            sys.exit("Thank you")
        elif productid == 1:
            category = get_categories()
        else:
            crt.add_item_to_cart(productid)
            
# print('3')        
def checkout_cart(cart):
    list_items_in_checkoutcart(cart)
    cprint('\n enter the number 1 to checkout and -1 to remove items from cart \n','red','on_white')
    option = int(input(""))
    if option == -1:
        deletesku = int(input("\nenter sku of the item that you want to delete \n"))
        with cart.conx as cursor:
            sql = "select * from cartitems where cartid = %s and sku = %s"
            count = cursor.execute(sql,(cart.id,deletesku))
            # count= cursor.fetchone()
            cursor.close()
        
        if count > 1:
            deletelimit = int(input("\nhow many do you want to delete \n"))
        else:
            deletelimit = 1
        with cart.conx as cursor:
            sql = "delete from cartitems where cartid = %s and sku = %s limit %s"
            deletedcount = cursor.execute(sql,(cart.id,deletesku,deletelimit))
            print ("%s items with sku %s were deleted from cart") %(deletelimit,deletesku)
            cursor.close()
        cart.conx.commit()
        # list_items_in_checkoutcart(cart) #listing all items in cart not 
        
    cart.put_items_in_cartitems()
    with cart.conx as cursor:
        sql = "update cart set ordered = 1 where cartid = %d" %(cart.id)
        cursor.execute(sql)
        cprint ("Checkout successful!!\n",'red','on_white')
        cursor.close()
    cart.conx.commit()
    # orders.place_order(cart.conx,cart.user,cart.id,items)
  

def browse_products(conx):
    with conx as cursor:
        
        # cursor = conx.cursor()
        sql = "select * from product"
        cursor.execute(sql)
        for i in cursor:
            print(i)
        cursor.close()
    
def add_to_cart(cart,productid):
    cart.add_item_to_cart(productid)
    
def review_purchase_history(conx,username):
    with conx as cursor:
        sql = "select cartid from cart where username = %(usrnm)s and ordered = 1 order by dts desc;"
        cursor.execute(sql,{'usrnm':username})
        recentorder = cursor.fetchone()
    cursor.close()
    if recentorder is not None:
        with conx as cursor:
            sql = "select sku from cartitems where cartid = %s" 
            cursor.execute(sql,recentorder)
            cprint ("\n recently purchased products : \n",'red','on_white') 
            for item in cursor:
                # print(item)
                dynamodb_service.get_item_from_dynamodb(item[0])
        cursor.close()
    

def list_items_in_checkoutcart(cart):
    cprint ("\n Items in cart : \n",'red','on_white') 
    items = cart.items
    for item in items:
        dynamodb_service.get_item_from_dynamodb(item)
        # print (item)
    if len(cart.saveditems):
        for saveditem in cart.saveditems:
            dynamodb_service.get_item_from_dynamodb(saveditem[0])
        
        
def get_categories():
    cprint('\nWhat are you looking for? Enter book, shoes or laptop \n','red','on_white')
    category = input("")
    cprint("\n products in that category: \n",'red','on_white')
    return category
        
