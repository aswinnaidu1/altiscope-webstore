from boto3.dynamodb.conditions import Key, Attr
import boto3

def get_item_from_dynamodb(sku):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1',aws_access_key_id='AKIAIPSVL4FEU2CDKXOQ',aws_secret_access_key='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')
    table = dynamodb.Table('Products')
    response = table.query(IndexName='SKU-index',KeyConditionExpression=Key('SKU').eq(sku))
    # for i in response[u'Items']:
        # print(json.dumps(i, cls=DecimalEncoder))
    print(response[u'Items'])
    
def get_from_dynamodb(category):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1',aws_access_key_id='AKIAIPSVL4FEU2CDKXOQ',aws_secret_access_key='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')
    table = dynamodb.Table('Products')
    response = table.query(KeyConditionExpression=Key('Category').eq(category))
    for i in response[u'Items']:
        # print(json.dumps(i, cls=DecimalEncoder))
        print(i)
