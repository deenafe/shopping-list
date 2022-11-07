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
    print(f"\n\nHi {customer_name}. We offer the best quality of consumables and groceries. Please find below, the item presently available in our store.\n")

    print("****************************")
    print("      Available Items")
    print("****************************\n")



display_available()