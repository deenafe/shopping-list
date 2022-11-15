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
