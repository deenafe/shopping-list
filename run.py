import gspread
from google.oauth2.service_account import Credentials

import pyfiglet

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
    welcome = pyfiglet.figlet_format("Welcome  to Deen's  Store")
    print(welcome)

    customer_name = input("Please enter your name: ")
    print(f"\n\nHi {customer_name}. We offer the best quality consumables and groceries." 
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
    while True:
        start_shopping = input("\n\nWould you like to start shopping now:(YES/NO) ")
        proceed_with_shopping = start_shopping.upper() == "YES"

        if proceed_with_shopping:
            print("\nPlease add the items you would like to purchase\n")
            break
        elif start_shopping.upper() == "":
            print("Please type in either YES or NO")
        elif start_shopping.upper() == "NO":       
             print("Thanks for visiting our store and we hope you shop with us soon.")
             break
        else:
            print("You entered an invalid word. Please enter YES or NO") 

    return proceed_with_shopping    
       

def shopping_items(available, proceed):
    """
    Takes input from user to select items to be purchased.
    Checks if the items selected is available in store.
    """
    shopping_cart = {}
    while proceed:
        add_items = input("Add items: ")

        if add_items.title() in available:
            add_quantity = int(input("Add quantity: "))
            for key, value in available.items():
                available[key] = float(value)
            shopping_cart.update({add_items: {"Quantity":add_quantity, "Subtotal": 
            available[add_items.title()]*add_quantity}})
            #round up subtoal to 2 decimal
            print(shopping_cart)
        elif add_items == "":
            print("You didn't add any items. Please select an item\n")
        else:
            print('The item selected is not available in our store\n')
        
        proceed = input("Do you wish to add more items (YES/NO): ")
        if proceed.upper() == "NO":
            # add elseif in case of invalid or blanks
            print("You have finished you shopping")
            break
        
    return shopping_cart


def bill_summary(items_bought):
    """
    Prints out summary of items and quantity bought.
    Prints out the subtotal for each items bought then it adds up
    the subtotal for each item to get the total value of items bought.
    """
    print("************************")
    print("     Bill Summary")
    print("************************\n")
    print("Item      Quantity       Subtotal")
    
    total = 0
    for key in items_bought:
        subtotal = round(items_bought[key]['Subtotal'], 2)
        print(f"{key}         {items_bought[key]['Quantity']}           {subtotal}")
        total = total + subtotal
        print(total)


available_in_store = display_available()
proceed_to_shopping = proceed_shopping()
lists_of_items = shopping_items(available_in_store, proceed_to_shopping)
print(lists_of_items)
bill_summary(lists_of_items)



