import pymysql
import boto3

def connecttodb():
    conx = pymysql.connect(host='dbanaidu.cjmvjfp6abln.us-east-1.rds.amazonaws.com',user='aswin',password='amazonsiva1',db='aircraftstore')
    conx.commit()
    return conx

def connecttodynamodb():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Products')
    return table
    
def get_info_from_dynamodb(sku):
    table = connecttodynamodb()
    response = table.query(IndexName='SKU-index',KeyConditionExpression=Key('SKU').eq(sku))
    # for i in response[u'Items']:
        # print(json.dumps(i, cls=DecimalEncoder))
    print(response[u'Items'])