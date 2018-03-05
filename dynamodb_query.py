from __future__ import print_function # Python 2/3 compatibility
import boto3
# import json
# import decimal
from boto3.dynamodb.conditions import Key, Attr

# def dynamodb_query(category,sku):
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Products')
category = 'shoes'
sku = 102

if sku:
    response = table.query(
        IndexName='SKU-index',
        KeyConditionExpression=Key('SKU').eq(sku)
        # & Key('SKU').eq(sku)
    )
else:
    response = table.query(
        
        KeyConditionExpression=Key('Category').eq('category')
    )

for i in response[u'Items']:
    # print(json.dumps(i, cls=DecimalEncoder))
    print(i)