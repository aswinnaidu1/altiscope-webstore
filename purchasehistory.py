import awsdbconnect
import dynamodb_service


def get_complete_history(username):
    conx = awsdbconnect.connecttodb()
    conx1 = awsdbconnect.connecttodb()
    with conx as cursor:
        sql = "select cartid from cart where username = %s and ordered = 1"
        rowcount = cursor.execute(sql,username)
        for item in cursor:
            print ("\n Items in order no : %s") %item[0]
            with conx1 as cursor1:
                sql1 = "select sku from cartitems where cartid = %s"
                skucount = cursor1.execute(sql1,item[0])
                for sku in cursor1:
                    dynamodb_service.get_item_from_dynamodb(sku[0])
            cursor1.close()
        cursor.close()
        
def get_recent_order(username):
    conx = awsdbconnect.connecttodb()
    conx1 = awsdbconnect.connecttodb()
    with conx as cursor:
        sql = "select max(cartid) from cart where username = %s and ordered = 1"
        rowcount = cursor.execute(sql,username)
        for item in cursor:
            print ("\n Items in recent order no %s") %item[0]
            with conx1 as cursor1:
                sql1 = "select sku from cartitems where cartid = %s"
                skucount = cursor1.execute(sql1,item[0])
                for sku in cursor1:
                    dynamodb_service.get_item_from_dynamodb(sku[0])
            cursor1.close()
        cursor.close()

if __name__ == "__main__":
    username = raw_input("Enter username: enter either wonderwoman, ironman or sully \n")
    # username = 'wonderwoman'
    get_recent_order(username)
    get_complete_history(username)
