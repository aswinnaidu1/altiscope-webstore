import awsdbconnect
# # # add product to the catalog
# # # provide product details below
dynamodbproduct = awsdbconnect.connecttodynamodb()
category = 'laptop'
sku = 304
name = 'samsung galaxy'
price = 1300
freeship = 1

# Insert the common attributes into MySQL
conx = awsdbconnect.connecttodb()
cursor = conx.cursor()
sql = "insert into product values(%s,%s,%s,%s)" 
param = (sku,name,price,freeship)
cursor.execute(sql,param)

# Insert the product info in a JSON format. Can include as many attributes as needed ans also any tags
response = dynamodbproduct.put_item(
  Item={
        'Category': category,
        'SKU': sku,
        'name': name,
        'brand': 'samsung',
        'screensize': 10,
        'tags': ['tablet','samsung','galaxy','etc'],
        'info': {
            'screen':"fifteeninches.",
            'color': 'white'
        }
    }
)

conx.commit()
print("Inserted the following product into catalog (both MySQL and DynamoDB) \n")
# print (response[u'Items'])
# commit only after both the insert (into MySQL) and put_item (into dynamo) are successful
