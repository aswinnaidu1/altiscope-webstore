import awsdbconnect

def place_order(conx,username, cartid,items):
    cursor = conx.cursor()
    # sql = "insert into orders(username,cartid) values(%(username)s,%(cartid)d)"
    # cursor.execute(sql,{'username':repr(username),'cartid':int(cartid)})
    dml_insert_order = "insert into orders(username) values(%(username)s)"
    cursor.execute(dml_insert_order,{'username':username})
    cursor.close()
    conx.commit()
    cursor = conx.cursor()
    cursor.execute("select max(orderid) from orders where username = %s",(username,))
    orderid = cursor.fetchone()[0]
    cursor.close()
    cursor = conx.cursor()
    dml_update_order = "update orders set cartid = %d where orderid = %d" %(cartid,orderid)
    
    cursor.execute(dml_update_order)
    cursor.close()
    cursor = conx.cursor()
    sql = "update cart set ordered = 1 where cartid = %d" %(cartid)
    cursor.execute(sql)
    conx.commit()
    # for item in items:
    #     sql = "insert into cartitems values(%d,%d)" %(cartid,item)
    #     cursor.execute(sql)
    conx.commit()
    print 'Order places successfully
    
    