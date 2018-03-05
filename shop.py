#shop the webstore
import sys
import awsdbconnect
import useractions
import cart
import purchasehistory
from termcolor import colored, cprint
# import cartface
conx = awsdbconnect.connecttodb()
dydbproducts = awsdbconnect.connecttodynamodb()
# authenticate username and password
cprint ("Enter username: enter either ironman or wonderwoman or sully", 'red','on_white')
username = raw_input("username: ")
# username = 'aviator'
#authenticate the user
valid = useractions.authenticate_user(conx,username)
if valid:
    print ('Welcome to the webstore')
else:
    sys.exit('invalid username, login again and enter valid username')

#once authenticated 
#check if a saved cart exists for this user
crt = cart.usercart(conx,dydbproducts)
crt.initialize_cart(username)
# useractions.browse_products(conx)
purchasehistory.get_recent_order(username)
useractions.go_shopping(conx,crt)


