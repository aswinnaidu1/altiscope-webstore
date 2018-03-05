# import cartitemsface
# get the recent cartid
def get_recent_cartid(conx,userid):
    cursor = conx.cursor()
    get_cartid = "select max(cartid) from cart where username = %(username)s"
    cursor.execute(get_cartid,{'username':userid})
    cur_tuple = cursor.fetchone()
    cartid = cur_tuple[0]
    cursor.close()
    return cartid
 
def create_cart(conx,userid):
# add cart
    cursor = conx.cursor()
    dml_insert_cart = "insert into cart values(NULL,%(userid)s)"
    cursor.execute(dml_insert_cart,{'userid':userid})
    # print prodid
    cursor.close()
    conx.commit()
    cartid = get_recent_cartid(conx,userid)
    return cartid

def checkout_cart(conx,cartid,userid):
    cursor = conx.cursor()
    dml_insert_cart = "insert into orders(username) values(%(userid)s)"
    cursor.execute(dml_insert_cart,{'userid':userid})
    dml_insert_cart = "update orders set `cartid` = %d" %(cartid)
    cursor.execute(dml_insert_cart)
    # dml_insert_cart = "insert into orders(orderid,username,cartid) values(null,?,?)" 
    # cursor.execute(dml_insert_cart,(userid,cartid))
    # print prodid
    cursor.close()
    conx.commit()
   
  
    