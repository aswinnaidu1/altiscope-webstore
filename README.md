---------------------------------------------------------------------------------------
------------------------------------- altiscope-webstore ------------------------------
---------------------------------------------------------------------------------------
Interview problem to design a backend webstore
This bare-bones version of the code contains the following microservices. Some of the related microservices are bundled into modules
1) shop.py: This script is the main script which calls all the microservices and acts similar to API gateway
2) User action: (useractions.py module) Includes services like authenticating user, checking user’s membership tier
3) Cart actions: (cart.py class) Includes services like adding items to cart, checking out cart, saving unchecked out carts,
    retrieving saved carts, showing items in a cart etc.
4) Catalog service: (dynamodb_service.py module) Includes services like providing paginated search results, providing info on
    products etc.
5) Adding products (add_products.py) to catalog is also implemented
6) Orders history service: (purchasehistory.py) Includes services like viewing recent orders, complete order history etc.
---------------------------------------------------------------------------------------
-----------------------------Code outline----------------------------------------------
---------------------------------------------------------------------------------------

1) Get the username and authenticate the user by checking the password
2) Check if the user has a saved cart? Go to the cart table and select the most recent cart under
this user that has not been checked out (ordered field will be 0) yet.
  a. If Yes, retrieve the saved cart and show the items: Get the skus’ of all items from the
cartitems table (in MySQL) and get product information from dynamoDB for all those
skus’
  b. If No, create a new cart for the user
  3) Show the recent purchase history for this user: From the cart table get the recent cartid for this
user which has been checked out (ordered set to 1) and join it with cartitems to get all skus’ in
this cart. Retrieve the product info for all these these skus’ from dynamoDB. (If required show
entire purchase history)
4) After reviewing saved cart and order history, let the user shop
5) Prompt the user for what he/she is looking for? Say, the user is looking for shoes. Query
dynamoDB for all items with partition key “shoes” and return the results with pagination. The
query returns 10-20 results per page and another 10-20 results for next page
6) The user can browse the results and search for another category of products. The user can add
products to the cart (in the code user has to enter the sku) and then the cart object adds this sku
to its list of products added.
7) The user can search for another product category, say laptop
8) As explained in 5) the products are returned to the user
9) The user can continue shopping and when he checks out, the cart table is updated (ordered is
set to 1) to show that the user has ordered the products. The cartitems table is also updated
with all the skus’ in that cart.
10) If the user logs out with checking out, then the cart table is updated (ordered field is set to 0) to
show that the cart is saved and cartitems table is updated with all skus’ in the cart.
