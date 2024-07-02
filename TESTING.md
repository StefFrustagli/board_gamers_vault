# The Boardgames Shelf - Testing details
[Main README.md file](README.md) <br>
[View the website on Heroku](https://the-boardgame-shelf-e0153506acf8.herokuapp.com/)

## Validator Testing

### HTML
All the HTML files were checked with [W3C Markup Validation Service](https://validator.w3.org/) and many of the errors identified appeared to be related to Django elements, so they were ignored.
These errors were acknowledged but not modified as they are integral to the correct functionality of the website.

### CSS

CSS files were checked with [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator.html.en) with no errors.

### JavaScript
JS files were checked with [JSHint](https://jshint.com/) with no errors.

### Python 
[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python code. All the errors highlighted were fixed. 

## Lighthouse Testing
I performed Lighthouse tests using Chrome Dev tools in an incognito window.


- **Homepage**:

    Initial results: 

    ![Homepage Lighthouse testing - initial results]()

    Current results:

    ![Homepage Lighthouse - current testing results]()

    Changes made:

- **Board on sale page**:

- **About page**:    
    Current results: 
    ![Topic page Lighthouse testing - current results]()

   Changes made: 



- **About page**:

    Current results:

    ![About page Lighthouse testing - current results]()

- **Register page**:

    Current results:

    ![Register page Lighthouse Testing - current results]() 

- **Login page**:

    Current results:

    ![Login page Lighthouse Testing - current results]()

- **Logout page**:

    Current results:

    ![Logout page Lighthouse Testing - current results]()


## Manual testing

| TO BE TESTED                      	| **TEST ACTION**                                                                                                                                                 	| **EXPECTED OUTCOME**                                                                                                                                                        	| **Expected outcome in details**                                                                                                                                                                                                                                                                                                          	| **TEST OUTCOME**                                                                                   	| **FURTHER ACTIONS**                                                                    	|
|-----------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|----------------------------------------------------------------------------------------------------	|----------------------------------------------------------------------------------------	|
| **Homepage &amp; Navigation Bar** 	| Access the website and you should be able to see the homepage. The Nav Bar is at the top. Use the scroll bar to scroll down and up if necessary.                	| All the elements of the homepage should be visible and responsive. By clicking on an element, it should redirect the user to the appropriate page or show a drop down menu. 	| The website title should be displayed in the top left corner of the page, and be replaced by a burger icon on tablets and smartphones.                                                                                                                                                                                                   	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| For non-registered users viewing the application on larger screens, the navigation bar should feature a "My Account" option. Clicking on this should reveal a dropdown menu offering options to "Register" or "Login". Conversely, for logged-in users, the navigation bar should display "Game Management", "My Profile", and "Logout". 	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| On tablets and mobile phones, the nav bar should display a hamburger icon that, when clicked, should display the same.                                                                                                                                                                                                                   	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| In larger screens, the nav bar should display Home, About, and Logout for logged-in users.                                                                                                                                                                                                                                               	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| On tablets and mobile phones, a burger icon should appear in the nav bar for logged-in users, allowing them to access Home, About, and Logout.                                                                                                                                                                                           	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| The shopping basket icon should remain visible at all times. Clicking on this icon should navigate the user to the Shopping Bag page.                                                                                                                                                                                                    	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| Clicking on "About the team" should redirect to the About page.                                                                                                                                                                                                                                                                          	|                                                                                                    	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| Clicking on the My Account dropdown menu options should correctly redirect to the appropriate page.                                                                                                                                                                                                                                      	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| If the website title is clicked on another page than the homepage, it should redirect to the homepage.                                                                                                                                                                                                                                   	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| The search bar should work correctly when a game is searched. If a game is not found, it should give the following result: 0 Games found for "game"                                                                                                                                                                                      	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| The search bar should give an error message if no search criteria is entered.                                                                                                                                                                                                                                                            	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| The 'On Sale,' 'Category,' and 'Condition' filters should correctly filter the items and redirect user to the 'Board Games on sale' page.                                                                                                                                                                                                	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| If in the brown banner "Sell an buy pre-owned board games!" is clicked, it should redirect to the homepage.                                                                                                                                                                                                                              	| Pass. It works as expected.                                                                        	|                                                                                        	|
| **Buttons in the Homepage**       	| Navigate to the white banner in the middle of the screen.                                                                                                       	| Two clickable buttons labeled "Board Games on Sale" and "Sell Your Game" should be displayed.                                                                               	| "Board games on sale" should redirect users to the marketplace.                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| "Sell your game" should redirect users to the page with the game addition form.                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
| **Footer**                        	| Access the website and scroll down to the bottom of the page.                                                                                                   	| The footer should be visible on all pages.                                                                                                                                  	| The footer should display the app's name, a brief description, social media links, contact details, and a privacy policy. Additionally, it should include a 'Subscribe to our newsletter' form (that disappears once the user subscribes).                                                                                               	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| Th Mailchimp Subscribe form should allow users to sign up to the newsletter by adding their email.                                                                                                                                                                                                                                       	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| The Privacy Policy link should open to another page and shows the policy.                                                                                                                                                                                                                                                                	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| The social media links should open in a new tab.                                                                                                                                                                                                                                                                                         	| Pass. It works as expected.                                                                        	|                                                                                        	|
| **"Board games on sale" page**    	| Navigate to the "Board games on sale" page using the brown button provided in the homepage.                                                                     	| All buttons and links should function correctly and perform the expected actions without errors.                                                                            	| Clicking on the image or "Details" should redirect the user to the Game Details page                                                                                                                                                                                                                                                     	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| A list of games on sale should be displayed with different information.                                                                                                     	| Every game should display the name, price, availability, a Details button, category, condition and seller's name.                                                                                                                                                                                                                        	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| The sort bar should provide various sorting options that function correctly and sort the items as described when selected.                                                                                                                                                                                                               	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| If the user is the seller of the game, an option to edit or delete the game should appear below that specific game.                                                                                                                                                                                                                      	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| The edit and delete options below a game should work as expected.                                                                                                                                                                                                                                                                        	| Failed. The edit option returned an error.                                                         	| This was FIXED by retrieving the game object first (see commit message for more info). 	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| When a game has been purchased, it should not appear in the "Games on sale" page anymore.                                                                                                                                                                                                                                                	| Pass. It works as expected.                                                                        	|                                                                                        	|
| **"Board game details" page**     	| Navigate to the "Board games on sale" page, then click on "Details" or on the image.                                                                            	| All buttons and links should function correctly and perform the expected actions without errors.                                                                            	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
| **Shopping Bag**                  	| Navigate to the basket icon on top of every page and click on it.                                                                                               	| Clicking on the "Secure checkout" button should redirect to the payment page.                                                                                               	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| Clicking on the "Keep shopping" should redirect to the Games on sale page.                                                                                                  	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| Below the total, an option to remove the item should appear and should remove the item when clicked.                                                                        	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
| **Checkout**                      	| Navigate from the homepage to the 'Board games on sale' page. Add a game to your basket, then click on 'Secure checkout' when the checkout window appears.      	| All buttons and links should function correctly and perform the expected actions without errors.                                                                            	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| If entered payment details (credit card number, CVV, expiration date), the purchase should be successful as expected.                                                       	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| In case of errors, the form validation should be displayed for incorrect inputs.                                                                                            	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| Throughout the checkout process, the order summary (items, quantities, prices) should remain accurate and updated.                                                          	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| After successful payment, the user should be redirected to a confirmation page displaying order details and a confirmation message.                                         	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| An email confirmation of the order should be sent to the user's registered email address after successful payment.                                                          	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| An email confirmation of the order should be sent to the seller's registered email address after successful payment.                                                        	|                                                                                                                                                                                                                                                                                                                                          	| This is yet to be implemented                                                                      	|                                                                                        	|
| **User's profile**                	| Navigate to "My account" in the nav bar and click on "My profile"                                                                                               	| When clicking 'Update', the personal details for 'City' and 'Favorite board games' should be updated.                                                                       	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| Previous orders should be displayed in the order history.                                                                                                                   	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
| **Register page**                 	| Access the website. If you are not logged in, you should be able to see 'Register' in the drop menu at the top of the screen, My account, when you click on it. 	| The Register page should show a form to register to the website.                                                                                                            	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| Users should be able to register by filling out all the required fields on the registration form.                                                                           	| When all fields are filled out correctly and submitted, a message should appear: "Successfully signed in as [username]".                                                                                                                                                                                                                 	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| The email field should be optional, so submissions can still be made without it.                                                                                                                                                                                                                                                         	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| Form submission should not be possible if a password that doesn't meet the criteria is entered.                                                                                                                                                                                                                                          	| PASS, but improvements needed. The reason why users are not logged in is not communicated to them. 	| The user should be notified with a message.                                            	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| The message "Filled out this field" should appear if a mandatory field is not filled out.                                                                                                                                                                                                                                                	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| A submit button should be available for submitting the registration.                                                                                                        	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
| **Login page**                    	| Access the website. If you are not logged in, you should be able to see 'Login' in the drop menu at the top of the screen, My account, when you click on it.    	| The Login page should show a form to register to the website.                                                                                                               	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| Users should be able to log in by filling out all the required fields on the form.                                                                                          	| When all fields are filled out correctly and submitted, a message should appear: "Successfully signed in as [username]".                                                                                                                                                                                                                 	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| The email field should be optional, so submissions can still be made without it.                                                                                                                                                                                                                                                         	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| Form submission should not be possible if a password that doesn't meet the criteria is entered.                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| The message "Filled out this field" should appear if a mandatory field is not filled out.                                                                                                                                                                                                                                                	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| An option to sign up should be available in the Login page if the user does not have an account.                                                                            	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
| **Logout page**                   	| Access the website. If you are logged in, you should be able to see 'Logout' in the drop menu at the top of the screen, My account, when you click on it.       	| A page should appear asking if the user is sure they want to sign out and a button to confirm.                                                                              	|                                                                                                                                                                                                                                                                                                                                          	| PASS, but improvements were needed to let the user cancel and return to the home page.             	| Added button to return to Homepage.                                                    	|
|                                   	|                                                                                                                                                                 	| By clicking signout, the user will be logged out.                                                                                                                           	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
| **About page**                    	| Access the homepage and navigate to the About page following the link in the navbar: "About the team".                                                          	| The About page should display the scope of the website and a feedback form.                                                                                                 	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
| **Feedback form**                 	|                                                                                                                                                                 	| The Feedback form should present a short text and three fields: Name, Email and Message.                                                                                    	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| Non-logged-in users should also be able to access the form.                                                                                                                 	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| All three fields must be filled out in order to submit the form.                                                                                                            	| By clicking on Submit, the form can be submitted if the three fields have been filled in.                                                                                                                                                                                                                                                	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| If a field is left blank, the form cannot be submitted and the user will be notified.                                                                                                                                                                                                                                                    	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	|                                                                                                                                                                             	| If the email field doesn't include "@", a message will be displayed asking the user to include it.                                                                                                                                                                                                                                       	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| Once the form is submitted, a confirmation message should appear.                                                                                                           	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
| **Django Admin Board**            	| Access the admin panel by adding 'admin' at the end of the website URL.                                                                                         	| There should be an authentication page that can only be accessed by admin users.                                                                                            	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| All admin user functionality should be displayed on the admin board.                                                                                                        	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| Admin users should be able to authorise new users' emails.                                                                                                                  	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| The Marketplace panel should allow Amins to add Games.                                                                                                                      	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|
|                                   	|                                                                                                                                                                 	| The About panel should allow admin users to add content in the About page.                                                                                                  	|                                                                                                                                                                                                                                                                                                                                          	| Pass. It works as expected.                                                                        	|                                                                                        	|



## User Stories completion

To check User Stories completion, please refer to the [Kanban Board](https://github.com/users/StefFrustagli/projects/3/views/1).

### User Stories - Acceptance Criteria testing

**[EPIC A] View and navigation**

**A1** - As a board games shopper, I want to be able to view a list of products available to purchase so that I can select the ones I want.

Acceptance criteria:
- [x] The user can access a page displaying a list of available products.
- [x] The product list is well-organised and easy to navigate.
- [x] Each product in the list includes essential information such as title, price, and image.

**Testing result**: Pass

**Further comments**: None

<br/>

**A2** - As a board games shopper, I want to be able to view individual product details so that I can identify the price, description, product condition and product image.

- [x] Users can click on a product from the list to view its detailed information.
- [x] The product detail page includes relevant information such as price, description, condition, and image.
- [x] The product detail page layout is user-friendly and visually appealing.
- [x] Users can easily navigate back to the product list or other parts of the website from the product detail page.

**Testing result**: Pass

**Further comments**: There is room for improvement in the layout and design of the product detail page.

<br/>


**A3** - As a board games shopper, I want to be able to easily view the total of my purchases at any time so that I can keep track of my spending and avoid overspending.

- [x] Users can see the total amount of their purchases displayed prominently on the website.
- [x] The total amount updates dynamically as users add or remove items from their shopping cart.
- [x] The total amount is easily visible and accessible from any page of the website.
- [x] Users can quickly understand their current spending status without any confusion.

**Testing result**: Pass

**Further comments**: None

<br/>

**A4** - As a board games shopper, I want to be able to access a 'search bar' so that I can see if the game I'm looking for is available.

- [x] The search bar is prominently displayed and easily accessible from any page of the website.
- [x] Users can enter keywords or phrases into the search bar to find specific products.
- [x] The search functionality returns relevant results quickly and accurately.
- [x] Users receive helpful feedback if no results are found or if there are any search errors.

**Testing result**: Pass

**Further comments**: None

<br/>

**A5** - As a board games shopper, I want to be able to filter products by various criteria (e.g., category, price, condition) so that I can easily find games that match my preferences.

- [x] The user can access a page with filter options to refine product selection by category, price range, and condition.
- [x] Filter options are prominently displayed and easy to locate on the product list page.
- [x] Selecting a category filter updates the product list to display only products in the chosen category.

**Testing result**: Pass

**Further comments**: None

<br/>

**[EPIC B] Registration and user account**

B1 - As a site user, I want to be able to easily register for an account so that I can have a personal account and view my profile.

- [x] Users can easily find the registration option on the website.
- [x] The registration process is intuitive, with clear instructions and minimal steps.
- [x] Users can input their personal information securely and efficiently.
- [x] Upon successful registration, users are redirected to their newly created personal account page.

**Testing result**: Pass

**Further comments**: None
<br/>

B2 - As a site user, I want to be able to easily login or logout so that I can access my account securely.

- [x] The login and logout options are easily accessible from any page of the website.
- [x] Users can securely log in using their registered email address and password.
- [x] The logout process is straightforward and clearly labeled.
- [x] Users are redirected to a relevant page after logging in or out, such as their personal account page or the homepage.

**Testing result**: Pass

**Further comments**: None
<br/>

**B3** - As a site user, I want to be able to easily recover my password so that I can always recover access to my account.

- [x] Users can easily find the password recovery option on the website.
- [x] The password recovery process is user-friendly and well-guided.
- [x] Users receive clear instructions on how to reset their password via email.
- [x] The password recovery process is secure and protects user privacy.

**Testing result**: Passed. Formatting issue was fixed in the template.

**Further comments**: None.
<br/>

B4 - As a site user, I want to be able to receive an email confirmation after registering so that I can verify that my account registration was successful. 

- [x] Users receive a prompt email confirmation after successfully registering for an account.
- [x] The email confirmation contains relevant information such as account details and verification instructions.
- [x] Users can easily verify their account registration by following the instructions provided in the email.
- [x] The email confirmation process is reliable and ensures that users can verify their accounts without any issues.

**Testing result**: Pass

**Further comments**: None
<br/>

B5 - As a site user, I want to be able to have a personalised user profile so that I can view my personal order history, order confirmations, and save my payment information. 

As a site user, I want to be able to have a personalised user profile so that I can view my personal order history, order confirmations, and save my payment information.

- [x] Users have access to a personalised user profile page after logging in.
- [x] The user profile page displays relevant information such as order history, order confirmations, and saved payment information.
- [x] Users can easily navigate and manage their personal profile settings.
- [x] The user profile page is visually appealing and user-friendly. 

**Testing result**: Pass, but this is still a work in progress.

**Further comments**: The User profile page can be improved.
<br/>

**B6** - As a site user, I want to have a public account that other users can access to see if I'm currently selling any games and my board games collection.

- [ ] The public account page displays information such as the user's current game listings and board game collection.
- [ ] Users can easily toggle their account visibility settings between public and private.
- [ ] The public account page provides valuable information for other users without compromising user privacy.

**Testing result**: Not Applicable - This hasn't been implemented yet.

**Further comments**: This is a future feature.
<br/>

**[EPIC C] Sorting and searching**

**C1** - As a board games shopper, I want to be able to search for a product by name so that I can easily find a specific game I'd like to purchase.

- [x] Users can easily find and access the search bar on the website.
- [x] The search functionality allows users to enter product names and find relevant results quickly.
- [x] Search results are accurate and display relevant products based on the search query.
- [x] Users receive helpful feedback if no results are found or if there are any search errors.

**Testing result**: Pass.

**Further comments**: None
<br/>

**C2** - As a board games shopper, I want to be able to sort a specific game by name so that I can easily find the best-priced or in best-condition specific game available.

- [x] Users can sort products by name in ascending or descending order.
- [x] Sorting options are easily accessible and clearly labeled on the product listing page.
- [x] The sorting functionality works smoothly and updates the product list dynamically.
- [x] Users can easily switch between different sorting options to find the products they are interested in.

**Testing result**: Pass, but this needs to be implemented as Name I've decided to consider at the moment. But users can do this by first searching for the name in the Search bar and then filtering.

**Further comments**: None
<br/>

**C3** - As a board games shopper, I want to be able to easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available.

- [x] After performing a search, users can easily see the search query and the number of results.
- [x]  Search results are displayed in a clear and organised manner, making it easy for users to review them.
- [x] Users can quickly navigate through search results and refine their search if needed.
- [x] The search results page provides helpful information to users, such as product names, prices, and images.

**Testing result**: Pass.

**Further comments**: None
<br/>

**C4** - As a board games shopper, I want to have convenient access to seller information so that I can feel confident about their credibility.

- [ ] Users can easily access seller information while browsing products.
- [ ] Seller information is prominently displayed on product detail pages.
- [ ] The seller information includes relevant details such as username, rating, and feedback score.
- [ ] Users can click on the seller's profile to view additional information and assess their credibility.

**Testing result**: Not Applicable. This feature hasn't been implemented yet.

**Further comments**: Future feature.
<br/>

**[EPIC D] Purchasing and checkout**

**D1** - As a board games shopper, I want to be able to easily select the item so that I can identify the total cost and the number of items I will receive.

- [x] Users can easily select items to add to their shopping bag.
- [x] The shopping bag displays the selected items along with their individual prices and quantities.
- [x] Users can view the total cost of their selected items, including any applicable taxes or shipping fees.
- [x] The total cost updates dynamically as users add or remove items from their shopping bag.

**Testing result**: Pass.

**Further comments**: None
<br/>

**D2** - As a board games shopper, I want to be able to view the items in my bag so that I can make sure that my purchase is correct.

- [x]  Users can easily access their shopping bag from any page of the website.
- [x] The shopping bag displays a summary of the selected items, including product names, prices, quantities, and total cost.
- [x] Users can easily review and edit the items in their shopping bag before proceeding to checkout.
- [x] The shopping bag provides clear instructions on how to proceed with checkout.

**Testing result**: Pass.

**Further comments**: None
<br/>

**D3** - As a board games shopper, I want to view an order confirmation after checkout so that I can verify that all is correct.

- [x] After completing the checkout process, users receive a clear and detailed order confirmation.
- [x] The order confirmation includes relevant details such as order number, items purchased, prices, and shipping information.
- [x] Users can easily review the order confirmation to verify that all information is correct.
- [x] The order confirmation page should provide instructions on how to track the order if possible, the seller and customer support. 

**Testing result**: Pass.

**Further comments**: Tracking feature not available yet, but it will be implemented in the future.
<br/>

**D4** - As a board games shopper, I want to receive an email configuration after checking out so that I can keep the confirmation of what I've purchased for my records.

- [x] Users receive a prompt email confirmation after successfully completing the checkout process.
- [x] The email confirmation contains relevant information such as order details, payment information, and shipping details.
- [x] Users can easily reference the email confirmation for their records or in case of any issues with their order.
- [x] The email confirmation should provide clear instructions on how to contact the seller and eventually tracking information. 

**Testing result**: Pass.

**Further comments**: Tracking feature not available yet, but it will be implemented in the future.
<br/>

**D5** - As a board games shopper, I want to view an order confirmation after checkout so that I can verify that all is correct.

- [x] Users can view a confirmation message immediately after completing checkout.
- [x] The order confirmation page displays a summary of the order, including item names, quantities, individual prices, and the total amount.
- [x] The order confirmation page includes the delivery address and payment method
- [ ] The order confirmation page includes the estimated delivery date. (Future feature)

**Testing result**: Pass, apart from the last Acceptance criteria that wasn't implemented yet.

**Further comments**: None.
<br/>

**[EPIC E] - Sale admin and store management**

**E1** - As a board games seller, I want to easily navigate to my sale account from which I can organise the products I intend to sell.

- [x] Sellers can easily navigate to their sale account from any page of the website.
- [x] The sale account interface provides a user-friendly dashboard for sellers to manage their products.
- [x] Sellers can access features such as adding new products, editing existing products, and deleting products from their sale account.
- [x] The navigation to the sale account is intuitive and clearly labeled for sellers to find easily.

**Testing result**: Pass, but this feature will be implemented in the future.

**Further comments**: This feature needs to be implemented. Currently users can add/edit/delete products to sell, but a sale account page needs to be implemented.

<br/>

**E2** - As a board game seller, I want the option to add one or more board games to sell so that I can sell more items at once.

- [x] Sellers have the option to add one or more board games to sell at once.
- [x] The add product functionality is accessible from the sale account dashboard.
- [x] Sellers can input relevant information for each product, such as title, description, price, condition, and image.
- [x] The add product process is straightforward and allows sellers to add multiple products efficiently.

**Testing result**: Pass.

**Further comments**: None

<br/>

**E3** - As a board games seller, I want to edit/update availability of a product so that I can change product criteria, like price, descriptions and images.

- [x] Sellers can easily edit and update the availability of their products from the sale account dashboard.
- [x] The edit/update functionality allows sellers to modify product criteria such as price, descriptions, images, and availability status.
- [x] Changes to product availability are reflected accurately and promptly on the website for shoppers to view.

**Testing result**: N/A as this feature will be implemented in the future.

**Further comments**: This feature needs to be implemented. Currently users can add/edit/delete products to sell, but a sale account page needs to be implemented.

<br/>

**E4** - As a board games seller, I want to be able to delete a product so that I can specify that that product is no longer available for sale.

- [x] Sellers have the ability to delete a product from their sale account when necessary.
- [x] The delete product functionality is easily accessible from the sale account dashboard.
- [ ] Sellers receive a confirmation prompt before permanently deleting a product to avoid accidental deletions.
- [x] Deleted products are removed from the website's product listings and marked as unavailable for sale.

**Testing result**: Pass. But the confirmation prompt will be added in the future.

**Further comments**: The confirmation prompt will be added in the future.
<br/>


## Automated testing
DA AGGIUNGERE
The functionalities tested were:
- Comments and collaboration forms;
- POST data and return of the correct response;
- Access to the topic page and the About page.

## Browser Compatibility
Below are the browsers that have been tested:
- Chrome Version 123.0.6312.87
- Firefox 118.0.2
- Safari Version 17.2.1

## Responsiveness 
The website's responsiveness has been tested using Google Chrome Developer Tools. To ensure compatibility across different devices, various screen resolutions were simulated. Custom media queries were implemented to address issues with some screen dimensions.
The website now displays responsively across a wide range of devices and screen sizes.

## Stripe Testing

To test the checkout process I have uses the Stripe test card details:

    Card number: 4242424242424242
    CVC: Any 3 digits
    Expiry: Any future date (eg. 04/25)

The test worked as expected.

## Bugs resolved

While working on this project, I encountered different bugs. Here are some of the bugs resolved:

1. Game addition logic in add_game view

This was a critical issue in the add_game view of marketplace/views.py. The logic for adding games did not properly validate form data before saving it to the database. This led to games being added even when form validation failed, resulting in inconsistent or incorrect data entries. This issue was addressed introducing conditional checks using form.is_valid() before calling form.save(), ensuring that game data is saved only when all required fields pass validation. Additionally, after a successful game addition, the view now redirects to a clean add_game form with a success message, enhancing user experience and clarity. Error messages are also displayed when validation fails, effectively notifying users of any issues preventing game additions. These changes collectively resolved the bug where games were erroneously added despite failing validation checks in the add_game view.

2. Issue with email variable rendering in email confirmation template

In the email confirmation template, the email variable was incorrectly split across lines, leading to improper rendering of the user's email address. The issue caused inconsistencies in how email addresses were displayed in confirmation emails, potentially confusing or misleading users. The fix involves ensuring that the email variable is correctly formatted and displayed within the template. 

## Remaining bugs

While there are various aspects of the app that require attention, to the best of my knowledge, there are currently no significant issues affecting the app's functionalities.