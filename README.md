################  webstore app for Altiscope  ####################
This code needs boto3, termcolor and pymysql packages, install them or run depend.py to install these above packages and then you're ready to run the code

-----------------------------instructions-------------------------
--------------- Running the code -----------------------------
Run shop.py and follow the prompts

Valid usernames are : ironman or wonderwoman or sully

if saved cart exist, it is listed now
and also any previous orders are also listed

Enter the category of products you're looking for
Search for products using these keywords only: book or shoes or laptop
A list of products in that category is listed.

When prompted
enter the sku of the products to add to cart. sku is the number in the product info after Decimal()
keep entering the skus' of products you want to add to cart.
To search for a new category of products enter 1

Enter a new keyword to search for products in that category.
Continue adding products and when ready to checkout enter 0
To proceed with the existing cart enter 1 or -1 to remove items
Right now you can only remove items once before it automatically checks out

To save cart and logout enter -1

---------------- Adding a product to catalog ---------------------------------------

To add a product to the catalog, change the input fields in the add_product.py script and run. (please
use a number greater than 500 for sku to avoid error (duplicate primary keys) in MySQL)
----------------- Purchase history ---------------------------------------------

To view purchase history of a user, edit the username variable in the purchasehistory.py and run the script








