import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('price_list')

def display_available():
    """
    Welcomes the customer to the online store.
    Request customer to input name, then displays items available in the store.
    Gets the available items from a worksheet.
    """
    print("****************************")
    print("Welcome to Deen's Online Store")
    print("****************************\n\n")

    customer_name = input("Please enter your name: ")
    print(f"\n\nHi {customer_name}. We offer the best quality of consumables and groceries." 
     + "Please find below, the item presently available in our store.\n")

    print("****************************")
    print("      Available Items")
    print("****************************")

    available = SHEET.worksheet("available").get_all_values()
    available_items = available[0]
    available_prices = available[1]
    
    available_dict = {}
    for items, prices in zip(available_items, available_prices):
        print(f"{items} (Price: {prices})")
        
    available_dict = dict(zip(available_items, available_prices))   
    
    return available_dict

def proceed_shopping():
    """
    Request input from user to start or exit shopping.
    """
    start_shopping = input("\n\nWould you like to start shopping now:(YES/NO) ")
    if start_shopping.upper() == "YES":
        print("\nPlease add the items you would like to purchase\n")
    elif start_shopping.upper() == "":
        print("Please type in either YES or NO")  
    elif start_shopping.upper() == "NO":
        print("Thanks for visiting our store and we hope you shop with us soon.") 
        #Call an exit function here 
    else:
        print("Please enter YES or NO") 

    return start_shopping       
       

def shopping_items(available):
    """
    Takes input from user to select items to be purchased.
    Checks if the items selected is available in store.
    """
    #Return to this function to add while and exit statement
    # while True:
    added_items = []
    add_items = input("Add items: ")
    if add_items in available:   
        print(f"Please select the quantity of {add_items} you wish to purchase ")
        added_items.append(add_items)
        print(added_items)
    elif add_items == "":
        print("You didn't add any items. Please select an item\n")
    else:
        print('The item selected is not available in our store\n')

    return added_items



available_in_store = display_available()
proceed = proceed_shopping()
shopping_items(available_in_store)