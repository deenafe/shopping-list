
""" API for Google Sheets."""
import gspread
from google.oauth2.service_account import Credentials


import pyfiglet

from colorama import Fore, Style


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('price_list')


def welcome():
    """
    Welcomes the customer to the online store.
    """
    welcome_to_store = pyfiglet.figlet_format("Welcome  to" +
                                              " Deen's Store",
                                              justify="center")
    print(welcome_to_store)

    customer_name = input("Please enter your name:\n ")
    while customer_name == "":
        customer_name = input(Fore.RED + "Please enter a name:\n ")
        print(Style.RESET_ALL)

    return customer_name


def display_available(customer):
    """
    Request customer to input name, then displays items available in the store.
    Gets the available items from a worksheet.
    """

    print(
          f'\nHi {customer.title()}. '
          'Thanks for choosing to shop with Deen"s Store. '
          'We offer the best quality consumables and groceries. '
          'Please find below, the items presently available in our store.\n'
        )

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


def validate_start_shopping_input():
    """
    Check for validity of user input to start or exit shopping.
    """

    while True:
        choice = input('Would you like to start shopping now: (YES/NO)\n ')
        if choice.upper() != "YES" and choice.upper() != "NO":
            print(Fore.RED + "You entered an invalid answer." +
                             " Please enter YES or NO")
            print(Style.RESET_ALL)
            continue
        else:
            break
    if choice.upper() == "YES":
        return choice
    elif choice.upper() == "NO":
        print("Thanks for visiting our store." +
              " We hope you shop with us soon.\n")
        exit()


def shopping_items(available, proceed):
    """
    Takes input from user to select items to be purchased.
    Checks if the items selected is available in store.
    Add items selected and quantity selected to a nested dictionary
    Calculates the subtotal for each item added
    Checkout from shopping after selecting all items needed
    """

    shopping_cart = {}
    print("\nPlease add the items you would like to purchase\n")

    while True:
        items = input("Add Items:\n ")
        if items.title() in available:
            try:
                quantity = int(input(f'How many {items.title()} do you wish to purchase: '))
            except ValueError:
                print("Please enter a number E.g.1,2,3,4,5...")
                continue

            for key, value in available.items():
                available[key] = float(value)
                shopping_cart.update(
                    {items:
                    {"Quantity": quantity,
                     "Subtotal": available[items.title()] *
                      quantity}
                    }
                )
            checkout = input("Do you wish to add more items (YES/NO):")
            while checkout.upper() != "YES" and checkout.upper() != "NO":
                print("Please enter YES or NO ")
                checkout = input("Do you wish to add more items (YES/NO):")

            if checkout.upper() == "YES":
                continue
            elif checkout.upper() == "NO":
                print("You have finished adding items to your shopping cart\n")
                break

        else:
            print(Fore.RED + "Your entry is not available in store," +
                             " Please check the list of available items ")
            print(Style.RESET_ALL)

        # try:
        #     quantity = int(input(f'How many {items.title()} do you wish to purchase: \n'))
        #     break
        # except ValueError:
        #     print(Fore.RED + 'You entered a Non-Number. ')
        #     print(Style.RESET_ALL)
        #     quantity = int(input(f'How many {items.title()} do you wish to purchase: \n'))

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
    bill_headers = ['Item', 'Quantity', 'Subtotal']
    print(f'{bill_headers[0]: <10}{bill_headers[1]: <15}{bill_headers[2]}')

    total = 0
    for key in items_bought:
        subtotal = round(items_bought[key]['Subtotal'], 2)
        print(f"{key}\t\t{items_bought[key]['Quantity']}\t  {subtotal}")
        total = total + subtotal
    print(Fore.GREEN + f"Your total bill is {round(total, 2)}\n")


def main():
    """
    Run all functions
    """
    name_of_customer = welcome()
    available_in_store = display_available(name_of_customer)
    start_shopping = validate_start_shopping_input()
    # proceed_to_shopping = proceed_shopping(check_start_shopping)
    lists_of_items = shopping_items(available_in_store, start_shopping)
    bill_summary(lists_of_items)


main()
