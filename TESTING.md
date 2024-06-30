# The Boardgames Shelf - testing details
[Main README.md file](README.md) <br>
[View the website on Heroku](https://the-boardgame-shelf-e0153506acf8.herokuapp.com/marketplace/)

## Validator Testing

### HTML
All the HTML files were checked with [W3C Markup Validation Service](https://validator.w3.org/) and errors identified addressed.

**Exclusions:**

Some errors involving Django elements, such as Summernote features or Bootstrap, were excluded. These errors were acknowledged but not modified as they are integral to the correct functionality of the website.



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



- **Topic pages**:    
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

Testing Stripe
To test the checkout process use the Stripe test card details:


## User Stories completion

To check User Stories completion, please refer to the [Kanban Board]().

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

**Testing result**: Pass

**Further comments**: None
<br/>

B2 - As a site user, I want to be able to easily login or logout so that I can access my account securely.

**Testing result**: Pass

**Further comments**: None
<br/>

**B3** - As a site user, I want to be able to easily recover my password so that I can always recover access to my account.

- [ ] Users can easily find the password recovery option on the website.
- [ ] The password recovery process is user-friendly and well-guided.
- [ ] Users receive clear instructions on how to reset their password via email.
- [ ] The password recovery process is secure and protects user privacy.

**Testing result**: Failed

**Further comments**: This needs further implementations as it gives an error at the moment.
<br/>

B4 - As a site user, I want to be able to receive an email confirmation after registering so that I can verify that my account registration was successful. 

**Testing result**: Pass

**Further comments**: None
<br/>

B5 - As a site user, I want to be able to have a personalised user profile so that I can view my personal order history, order confirmations, and save my payment information. 

**Testing result**: Pass

**Further comments**: None
<br/>

B6 - As a site user, I want to have a public account that other users can access to see if I'm currently selling any games and my board games collection.

**Testing result**: Pass

**Further comments**: None
<br/>

**[EPIC C] Sorting and searching**

C1 - As a board games shopper, I want to be able to search for a product by name so that I can easily find a specific game I'd like to purchase.

C2 - As a board games shopper, I want to be able to sort a specific game by name so that I can easily find the best-priced or in best-condition specific game available.

C3 - As a board games shopper, I want to be able to easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available.

C4 - As a board games shopper, I want to have convenient access to seller information so that I can feel confident about their credibility.

**[EPIC D] Purchasing and checkout**

D1 - As a board games shopper, I want to be able to easily select the item so that I can identify the total cost and the number of items I will receive.

D2 - As a board games shopper, I want to be able to view the items in my bag so that I can make sure that my purchase is correct.

D3 - As a board games shopper, I want to view an order confirmation after checkout so that I can verify that all is correct.

D4 - As a board games shopper, I want to receive an email configuration after checking out so that I can keep the confirmation of what I've purchased for my records.

**[EPIC E] - Sale admin and store management**

E1 - As a board games seller, I want to easily navigate to my sale account from which I can organise the products I intend to sell.

E2 - As a board game seller, I want the option to add one or more board games to sell so that I can sell more items at once.

E3 - As a board games seller, I want to edit/update availability of a product so that I can change product criteria, like price, descriptions and images.

E4 - As a board games seller, I want to be able to delete a product so that I can specify that that product is no longer available for sale.




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



## Remaining bugs

There are no major issues that impact the website's functionalities. 