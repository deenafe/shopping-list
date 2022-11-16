# **DEEN'S STORE**

Deen's Store is a Python program for a self service interactive kiosk.   The Self service kiosk is for a virtual grocery and consumable store and it runs on Heroku.

The live project can be viewed [here]( https://deens-store.herokuapp.com/)

For most people, going shopping can be a long, tedious process. It’s a fact of life that time is precious and consumer's who go about their day-to-day shopping would value convenient and time-saving solutions to their shopping experience.

Rather than waiting on long lines of queues to make money transactions and complete a shopping experience, a consumer can complete the entire process of familiarizing and buying products in the store without having to wait for attention from the store's personnel. 

The self service kiosk program aims to reduce transaction time, improve customer service, and providing a personalized shopping experience.
***



## Shopping Experience

With Deen's Store self service kiosk, users can start their shopping experience by inputting their name, upon which a welcome message is displayed followed by a listing of the items currently available in the store, with the prices of each item also on display. The user goes through the list of items available to determine what items they will like to purchase and can proceed to select the items. 

With each item selection, the user is also required to state the quantity they wish to purchase for each item. Users also get a request to continue or discontinue shopping after each item selection. If they wish to continue, they are asked to add other items they wish to purchase and if they wish to checkout, the cost of all the items selected will be calculated and a bill summary will be printed to the terminal.


## Features

**Title Section:**

* [Pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/#:~:text=pyfiglet%20takes%20ASCII%20text%20and,pyfiglet%20module%20%3A%20pip%20install%20pyfiglet) was installed and import pyfiglet was used to generate ASCII art for the title displaying the name of the store.

* Standard Font was used for the title as it is large and has nice spacing and clarity of letters. It was centred to give a nice clean layout too.

* Below the title is a message to the user to enter their name. This prompts the user to start shopping on the digital kiosk.

![](/assets/images/store-title.png)




**Name Input Section:**

* If the user presses enter without inputting a name, another input message with a red text colour will display alerting the user that a name must be entered.

* After the user inputs a name, they are greeted with a personalized welcome message. The Welcome message also seeks to assure the user that the products available in the store are of good quality.  

* Below the welcome message is a list of all items and prices currently available in the store. The items and prices are obtained from a spreadsheet linked with an API. Any changes made to the store's spreadsheet that updates the list of items available and prices would reflect on the Available Items displayed on the self service kiosk.

![](/assets/images/name_error.png)

![](/assets/images/welcome_message.png)

![](/assets/images/available_items.png)

**Start Shopping Input Validation:**

* After going through the store's available items and prices, the user is then asked if they will like to start shopping by indicating YES or NO

* If the user input is neither YES or NO, an error message highlighted in red is printed informing the user that an invalid word was entered. If the user simply presses enter without inputting YES or NO, an error message highlighted in red is printed asking the user to type in either YES or NO.

* If the user's answer is NO, then a message is printed thanking the user for visiting the store and imploring them to come back another time to shop at the store.

![](/assets/images/start_shopping.png)

![](/assets/images/start_shopping_error1.png)

![](/assets/images/start_shopping_error2.png)

![](/assets/images/start_shopping_no.png)




**Add Items Input Validation:**

* After a user agrees to start shopping by inputting YES, a message is printed asking the user to add the items they wish to purchase from the store. Then an input request is made to enter the first item they will like to purchase.

* If a user simply presses enter without typing in any item, an error message highlighted in red is printed informing the user they didn't add any items. Then an input request is made to ask if the user wishes to add other items.

* If a user enters an item that is not available in the store, an error message highlighted in red is printed informing the user that the added item is not available in the store. Then an input request is made to ask if the user wishes to add other items.

![](/assets/images/add_items.png)

![](/assets/images/add_items_empty.png)

![](/assets/images/add_items_unavailable.png)


**Add Quantity Input:**

* Any added item is checked for in-store availability and if available, the user is asked to input the quantity they wish to purchase for the added item.

* Upon inputting the quantity for a selected item, the user is asked if they wish to continue shopping by a YES or NO input to add another item. If the type in YES they get prompted to add an item, then quantity for the entered item.

![](/assets/images/add_quantity.png)

![](/assets/images/more_items.png)


**Continue Shopping Feedback:**

* After each item and quantity input, the user can continue adding items till they input NO to stop adding more items.

* The price of each item added is multiplied by the quantity entered, to get the Sub-total for each item added. For example:
   Bread (Price: 3.15)
   If the quantity of bread entered is 3. The total amount for the added item will be 3.15 x 3 = 9.45

   ![](/assets/images/continue_shopping.png)


**Finished Shopping Feedback:**

* Once a user enters NO to the input request for continue adding other items, it means the user is done shopping and a message is printed informing the user that they having finished adding items to their shopping cart.

![](/assets/images/finish_shopping.png)


**Final Bill:**

* With the user done adding items, the total bill is calculated by adding the subtotals for all the added items. The final bill summary is printed to displaying to the user in rows and columns, the items bought, quantity for each items bought and the sub total for each items bought. 

* A total bill is then printed to the user highlighted in green.

![](/assets/images/total_bill.png)


### Future Development & Features Left to Implement

* When the user opts to stop adding items to their shopping cart by entering NO to the YES or NO input request, instead of proceeding to calculate their final bill, I would like to have another prompt message printed to the user, asking the user if they are sure they are done with adding items with another YES or NO input request. To reconfirm they wish to quit, they should input NO and if they still want to continue adding items they can input YES. This reconfirmation prompt message will allow the user to reconsider if they wish to add more items before checking out to the bill summary.

* Every store owner will want to have records of goods sold, so it would be very useful to have data of the from the bill summary posted to a Google spreadsheet, with following details in the first row of the worksheet: Customer Name, Item Bought, Quantity Bought, Amount, Date. This information would be very helpful to the store owner/management.

**Flow Control**

The flow of execution of the program captures how statements, conditions and function calls are executed in sequence one after another to maintain the order of the program. The flow control chart of the program was laid out and structured to aid in the design of the control flow statements such as if-elif-else statements, while loops and for loops.  This also allowed the design of the user input validation checks to be visually clear before the code was written.

![](/assets/images/deens-flowchart.jpg)


**Fonts**
[Pyfiglet](https://pypi.org/project/pyfiglet/0.7/) was installed and import pyfiglet was used to generate ASCII art for the title message.  Pyfiglet was added to requirements.txt for deployment to Heroku.

**Colour**
To change the font colour and background colour of some words [Colorama](https://pypi.org/project/colorama/) was imported.  Colorama was added to requirements.txt then for deployment.


## Libraries & Technology Used

*   gspread

The gspread library was imported to make use of the Credential class and to enable interaction with Google sheet API credentials on the creds.json file.

*   [Pyfiglet](https://pypi.org/project/pyfiglet/0.7/) 

This was used to add ASCII art to the title message

* [Colorama](https://pypi.org/project/colorama/) 

This was used to add colour to fonts and provide visual notification to the user.

*   [LucidCharts](https://www.lucidchart.com/) 

This was used to create the Flowchart.

*   Windows Sniiping tool.

This was used to screenshot and save images of the running program and flow chart. 






