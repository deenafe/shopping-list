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

* [Pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/#:~:text=pyfiglet%20takes%20ASCII%20text%20and,pyfiglet%20module%20%3A%20pip%20install%20pyfiglet) was installed and pyfiglet was used to generate ASCII art for the title displaying the name of the store.

* The title fonts were centered to give a nice clean layout too.

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

* If a user inputs a quantity that is not a number or simply presses enter without entering any input value, an error message highlighted in red is printed informing the user they entered a Non-Number and asks the user to re-enter a number giving an examples of a number entry.

* Upon inputting the quantity for a selected item, the user is asked if they wish to continue shopping by a YES or NO input to add another item. If the type in YES they get prompted to add an item, then quantity for the entered item.

![](/assets/images/non_number_quantity.png)

![](/assets/images/blank_number_quantity.png)

![](/assets/images/add_quantity.png)

![](/assets/images/more_items.png)


**Continue Shopping Feedback:**

* After each item and quantity input, the user can continue adding items till they input NO to stop adding more items.

* The price of each item added is multiplied by the quantity entered, to get the Sub-total for each item added. For example:
   Bread (Price: 3.15)
   If the quantity of bread entered is 3. The total amount for the added item will be 3.15 x 3 = 9.45. This information is not printed to the terminal but provided the basis for calculating the bill summary after user is done shopping.

   ![](/assets/images/continue_shopping.png)


**Finished Shopping Feedback:**

* Once a user enters NO to the input request for continue adding other items, it means the user is done shopping and a message is printed informing the user that they having finished adding items to their shopping cart.

![](/assets/images/finish_shopping.png)


**Final Bill:**

* With the user done adding items, the total bill is calculated by adding the subtotals for all the added items. The final bill summary is printed to displaying to the user in rows and columns, the items bought, quantity for each items bought and the sub total for each items bought. 

* A total bill is then printed to the user highlighted in green.

![](/assets/images/total_bill.png)


### Future Development & Features Left to Implement

* When the user opts to stop adding items to their shopping cart by entering NO to the YES or NO input request, instead of proceeding to calculate their final bill, I would like to have another prompt message printed to the user, asking the user if they are sure they are done with adding items with another YES or NO input request. To reconfirm if they wish to quit, they should input NO and if they still want to continue adding items they can input YES. This prompt message will allow the user to reconsider if they wish to add more items before checking out to the bill summary.

* Every store owner will want to have records of goods sold, so it would be very useful to have data from the bill summary posted to a Google spreadsheet, to be populated with the following details as headers in the first row of the worksheet: 

   * Customer Name
   * Item Bought
   * Quantity Bought
   * Amount
   * Date 

This information would be very helpful to the store owner/management.


**Flow Control**

The flow of execution of the program captures how statements, conditions and function calls are executed in sequence one after another to maintain the order of the program. The flow control chart of the program was laid out and structured to aid in the design of the control flow statements such as if-elif-else statements, while loops and for loops.  This also allowed the design of the user input validation checks to be visually clear before the code was written.

![](/assets/images/deens-flowchart.jpg)


**Fonts**
[Pyfiglet](https://pypi.org/project/pyfiglet/0.7/) was installed and import pyfiglet was used to generate ASCII art for the title message.  Pyfiglet was added to requirements.txt for deployment to Heroku.

**Colour**
To change the font colour and background colour of some words [Colorama](https://pypi.org/project/colorama/) was imported.  Colorama was added to requirements.txt then for deployment.


## Libraries & Technologies Used

*   gspread

The gspread library was imported to make use of the Credentials class and to enable interaction with Google sheet API credentials on the creds.json file.

*   [Pyfiglet](https://pypi.org/project/pyfiglet/0.7/) 

This was used to add ASCII art to the title message

* [Colorama](https://pypi.org/project/colorama/) 

This was used to add colour to fonts and provide visual notification to the user.

*   [LucidCharts](https://www.lucidchart.com/) 

This was used to create the Flowchart.

*   Windows Snipping tool.

This was used to screenshot and save images of the running program and flow chart.

*   Github

This was used to host the Code for the project and the project was project was developed utilising the [Code Institute Template]( https://github.com/Code-Institute-Org/python-essentials-template).

*   Gitpod Workspace

This is the developer environment where the code for this project was written, added, committed and pushed to the Github repository.



## Testing
*   Methods such as print() as the code developed was used to check for errors.  This helped check that for loops, arguments passed to functions and function return values were working as expected.

*   Errors or warnings were such as indentation errors, lines too long or extra space issues, traceback errors etc. were fixed as the code for the program was being written. This helped keep the code clean and readable.

*   The inputs were tested to ensure user inputs would be handled correctly and appropriate feedback to the user was displayed on screen.  The Features Section above sheds light on how the user inputs were handled and the following actions were taken to test the inputs

    *   Customer Name:
    This accept any input of characters except blanks. The enter key was pressed without typing in anything to the input request to ensure error was caught and handled appropriately.

    *   Start Shopping:
    To test the start shopping input, a random word other than YES or NO was inputted, then a blank by pressing the enter key without entering a word. This was done to ensure error is caught and handled appropriately.   

    *   Add Items:
    To test the add items input, a blank is inputted by pressing the enter key without entering a word. Then a random word was entered to ensure errors were caught and handled appropriately.

    *  Add Quantity:
    To test the add quantity input, a blank is inputted by pressing the enter key without entering a word. Then a random alphabet or word was entered to ensure errors were caught and handled appropriately.

*   The README.md was proofread, using Microsoft Office spell check and all links were checked before final submission.    


## Bugs

### Identified Bugs

* ValueError: invalid literal for int() with base 10:

    * During testing, I discovered that the add_quantity Input would throw up an error and exit the program if a blank Input or Non-Number is entered.

>
>  File "run.py", line 104, in shopping_items
>
>   add_quantity = int(input(f'How many {add_items.title()}'
>
> ValueError: invalid literal for int() with base 10: 'w'


    To resolve this, I used a try/except statement to handle the error and alert the user if a Non-number or blank Input is entered. Following the message alerting the user to the error, an Input request is made again, this time providing examples of a number.


### Unfixed Bugs


### Validator Testing

A PEP8 validator already installed on my Gitpod Workspace was used for code validation. The following steps were taken to validate the code.

*  Pressed Ctrl+Shift+P on the Keyboard
* On the search Bar that appeared in the workspace, typed in the word > Linter
* From the options that appeared below the Search Bar, clicked on > Python: Select Linter
* Selected > pycodestyle from the options displayed.

The code showed no errors after the above mentioned steps were done.


## Deployment

The site was deployed via [Heroku]( https://id.heroku.com/login), and the live link can be found here: [Deen's Store](https://deens-store.herokuapp.com/) 

Before deploying to Heroku pip3 freeze > requirements.txt was used to add dependencies and imports for deployment.

1.	Log in to [Heroku]( https://id.heroku.com/login) or create an account if required.
2.	Then, click the button labelled **New** from the dashboard in the top right corner and from the drop-down menu select **Create New App**.
3.	You must enter a unique app name, (I used mastermind-code-breaker).
4.	Next, select your region, (I chose Europe as I am in Ireland).
5.	Click on the **Create App** button.
6.	The next page you will see is the project’s Deploy Tab.  Click on the **Settings Tab** and scroll down to **Config Vars**.
7.	Click **Reveal Config Vars** and enter **port** into the **Key** box and **8000** into the **Value** box and click the **Add** button.
8.	Next, scroll down to the Buildpack section click **Add Buildpack** select **python** and click **Save Changes**.
9.	Repeat step 8 to add **node.js**.
o	**Note:** The Buildpacks must be in the correct order. If not click and drag them to move into the correct order.
10.	Scroll to the top of the page and now choose the **Deploy** tab.
11.	Select **Github** as the deployment method.
12.	Confirm you want to connect to GitHub.
13.	Search for the repository name and click the connect button.
14.	Scroll to the bottom of the deploy page and select preferred deployment type:

* Click either **Enable Automatic Deploys** for automatic deployment when you push updates to Github.

* Select the correct branch for deployment from the drop-down menu and click **Deploy Branch** for manual deployment.


## Credits  

Some tutorials and resources which I used for guidance in coding this project are:

*  A [Youtube Tutorial video](https://www.youtube.com/watch?v=IH4tog2DHt4) perfectly captured the idea of what I was trying to implement and code from this tutorial was borrowed for this project.

*  The Love Sandwiches 05 tutorial video was helpful in recalling how to connect the API to the project code.

*  The Love Sandwiches 05 tutorial video was helpful in recalling how to connect the API to the project code.

*  [Print Colors in Python terminal](https://www.geeksforgeeks.org/print-colors-python-terminal/)

*  [Pyfiglet in Python](https://www.codespeedy.com/pyfiglet-in-python/)

*  [Python | ASCII Art Using pyfiglet Module](https://www.codespeedy.com/pyfiglet-in-python/)

*  [Python Dictionary Comprehension](https://www.geeksforgeeks.org/python-dictionary-comprehension/)

*  [Python Dictionary Comprehension](https://www.programiz.com/python-programming/dictionary-comprehension)

## Acknowledgement

I am particularly grateful for the advice and support of my Mentor, Daisy, who was of tremendous assistance in guiding me through the grey areas of the project.
