# The Board Games Vault

Developer: Stefania Frustagli

## Website Overview



#### Why a Board Games Vault?

IT DOESNT LOOK LIKE THERE IS A DECENT WEBSITE WHERE TO SELL USED BOARD GAMES AND create a catalogue of board games owned.  SO I DECIDED TO CREATE AN E-COMMERCE TO ALLOW USERS TO SELL THEIR OWN BOARD GAMES. 
SELLERS CAN ADD THEIR LOCATION SO THAT BUYERS CAN SEE IF THE TRANSACTION IS POSSIBLE.
A future development will allow users to create their own database, public or private, where to catalogue the games they owe, the games they want to sell, the games they wish to buy, the games they played and reviewing games.

View the live project [here]().

## Table of Contents DA MODIFICARE

- [Website Overview](#website-overview)
- [Project background](#project-background)
  - [Agile Development](#agile-development)
  - [Problem Statement](#problem-statement)
  - [The Design Process](#the-design-process-thinking-through-it)
  - [Colour Palettes](#colour-palettes)
  - [Fonts](#fonts)
  - [Wireframes](#wireframes)
  - [Data Model](#data-model)
- [User Experience](#user-experience)
  - [Ideal Users](#ideal-users)
  - [User Stories](#user-stories-site-accessibility--functionality)
- [Features and functionalities](#features-and-functionalities)
  - [Current Features](#current-features)
  - [Future Features](#future-features-and-general-aspects-left-to-implement)
- [Technologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## Project background

### Agile Development

The development process for this project followed Agile methodology, emphasizing continuous improvement throughout the development lifecycle.

**Project Management**: I utilised GitHub Project boards to manage tasks, user stories, and project progression effectively.

DA MODIFICARE

**User Stories**: User stories were categorized in a Kanban Board into EPICs A, B, C, D, E, and F based on user types and content specificity. I prioritized user stories using the MoSCoW method, which categorizes requirements into Must have, Should have, Could have, and Won't have categories based on their importance and urgency.

[Link to the GitHub Project board]()

**Continuous Improvement**: Despite working solo on this project, I actively sought ways to enhance development processes and product quality. Regular retrospectives allowed me to reflect on past work, pinpoint areas for improvement, and brainstorm solutions.

### Problem Statement

CREARE UNA LIBRERIA PER BOARD GAMERS PER AGGIUNGERE I LORO GIOCHI - ES. GOODREADS, ANOOBI
E PERMETTERE LORO DI VENDERE I LORO GIOCHI

I've noticed that among board gamers 'fanatic' collect board games is common and buy them is almost a compulsively act. And it is common for them to get rid of games they don't play anymore. Instead of using ebay, I wanted to create a specific place for this. And create a library of games.

TO BE MODIFIED

**Proposed solution**: 

### The design process: thinking through it



### Fonts
Fonts used are TO BE ADDED 
They were imported using Google fonts.

### Colour palettes

![Colour Palette]()



### Wireframes

**Homepage** [Desktop and mobile]:

![Wireframe created using Balsamiq - Homepage on Desktop](https://i.ibb.co/LgY3Tb8/my-screenshots-2024-05-13-at-22-05-39.png)

![Wireframe created using Balsamiq - Homepage on Mobile](https://i.ibb.co/4Tj1tdN/my-screenshots-2024-05-13-at-22-05-28.png)


About page [Desktop and mobile]:

![Wireframe created using Balsamiq - About page]()

Register page [Desktop and mobile]:

![Wireframe created using Balsamiq - Register]()

Login page [Desktop and mobile]:

![Wireframe created using Balsamiq - Login]() .
  
**Basket page** [Desktop and mobile]:

![Wireframe created using Balsamiq - Basket page template for desktop](https://i.ibb.co/hsPwrcX/my-screenshots-2024-05-13-at-22-06-11.png)

![Wireframe created using Balsamiq - Basket page template for mobile](https://i.ibb.co/q00vPqF/my-screenshots-2024-05-13-at-22-05-58.png)

**User Account page** [Desktop and mobile]:

![Wireframe created using Balsamiq - User Account page on desktop](https://i.ibb.co/rbhX9s6/my-screenshots-2024-05-13-at-22-05-19.png)

![Wireframe created using Balsamiq - User Account page on mobile](https://i.ibb.co/pPztmXN/my-screenshots-2024-05-13-at-22-05-06.png)

**Board game description page** [Desktop and mobile]:

![Wireframe created using Balsamiq - User Account page on desktop](https://i.ibb.co/TwL0B2M/my-screenshots-2024-05-15-at-18-12-43.png)

![Wireframe created using Balsamiq - User Account page on mobile](https://i.ibb.co/sqsjyx7/my-screenshots-2024-05-15-at-18-12-30.png)

### Data Model 

EXPLAIN THE RELATIONSHIP BETWEEN THE MODELS

The structure of our database was illustrated using an Entity-Relationship Diagram (ERD). This diagram shows how different entities within the system are related to each other and helps in understanding the data flow. 

**ERD**:
![ERD]()
ADD IMAGE OF DIAGRAM

**Models**

1. **User Profile**: 
   - This model extends Django's built-in User model to include additional fields like a profile picture, contact information.
   - This model represents both buyers and sellers.

2. **Game**:
   - This model represents individual board games available for sale.
   - Attributes: 
     - Title
     - Description
     - Image (for the cover or a picture of the game)
     - Price
     - Condition (e.g., new, used - you might want to use choices for this)
     - Seller (ForeignKey to User Profile)

3. **SellerAccount**: 
   - This model represents the seller's account information.
   - Attributes:
     - User (OneToOneField to User Profile)
     - Payment information (could include fields like PayPal email, bank details, etc.)

4. **BasketItem**:
   - This model represents items added to a user's basket.
   - Attributes:
     - User (ForeignKey to User Profile)
     - Game (ForeignKey to Game)
     - Quantity
     - Total price (could be calculated based on the quantity and the game's price)



Draft flowchart for apps organisation:
![draft flowchart to organise apps](ht)

The **applications** used are:

1. Main app: board_gamers_vault 

This is the main app that contains project-level settings, URLs, and any global templates and static files.

2. Store App

This app handles all functionalities related to the e-commerce store, including models for games, user profiles, seller accounts and basket items.

3. User Management App

This app handles user authentication, registration, profile editing, and other user-related functionalities.

## User Experience

#### Ideal users: DA FINIRE

- Board game shopper: someone who wants to buy or sell a pre-owned board game.

#### As a developer, I expect:

DA AGGIUNGERE

### User Stories

**[EPIC A] View and navigation**

A1 - As a board games shopper, I want be able to view a list of products available to purchase so that I can select the ones I want.

A2 - As a board games shopper, I want be able to view individual product details so that I can identify the price, description, product condition and product image.

A3 - As a board games shopper, I want to be able to easily view the total of my purchases at any time so that I can keep track of my spending and avoid overspending.

A4 - As a board games shopper, I want be able to access a 'search bar' so that I can see if the game I'm looking for is available.

**[EPIC B] Registration and user account**

B1 - As a site user, I want to be able to easily register for an account so that I can have a personal account and view my profile.

B2 - As a site user, I want to be able to easily login or logout so that I can access my account securely.

B3 - As a site user, I want to be able to easily recover my password so that I can always recover access to my account.

B4 - As a site user, I want to be able to receive an email confirmation after registering so that I can verify that my account registration was successful. 

B5 - As a site user, I want to be able to have a personalised user profile so that I can view my personal order history, order confirmations, and save my payment information. 

B6 - As a site user, I want to have a public account that other users can access to see if I'm currently selling any games and my board games collection.

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

## Features

### Current Features


#### Navbar


![Website name]()

The navigation links are: 






#### Authentication and notification messages
Users can see their log status below the navigation bar. The following message will appear to the right of the acreen if users are logged in:

"You are logged in as [username]" 

Otherwise, a message stating they are not logged in will apprear, with a link:

"You are not logged in.
Log *here*."

Below the navigation bar will also appear other notifications, such as sign out, edits and deletions of comments.

Example:
![Sign out confirmation message]()

#### Footer
On every page, the footer displays 
ADD
![Footer](https://)

#### Homepage


![Homepage]()




#### Register page
The Register page, which is visible to non-logged-in users, presents a registration form. The mandatory fields are 'Username' and 'Password' (to be entered twice), while the optional field is 'Email' address.

![Register page]()
In addition, it contains a link that leads to the Login page, if the user has already created an account.

#### Sign in page
The Sign in page allows registered users to sign into their account by entering their username and password. It also contains a link to the Register page, if the user hasn't created an account yet.
![Sign-in form]()

Also, users have the option of having their login information remembered, so they don't have to re-enter their login details each time they visit the website.

#### Logout page
The logout page allows users to log out of their accounts. The user must confirm their choice. They  can also cancel the action and return to the homepage.

![Log out form]()


#### About page
This page outlines the purpose of the website and my role as a creator. The purpose of my short presentation is to establish trust with the viewer and to explain the current state of the website in a clear and concise manner.

![About section explaining the purpose of the website](https://)


#### Django admin board
The admin board allows administrators to control the website. They can add topics and contents, edit the About section and authorise comments to be published.

![Django Administrator Board]()

In the admin board, it is also possible to control users' permissions, deactivate their accounts or make them admin users.

The functionalities are still basic and will be improved in the future.

#### Favicon
TO BE ADDED

![Favicon]()

#### Error pages
The error pages simply provide the user with a link back to the homepage and inform them what type of error they encountered.

### Future Features and general aspects left to implement

TO BE ADDED

## Technologies used

### Programming Languages

- Programming languages used in this project are **HTML5**, **CSS3**, **JavaSctipt** and **Python**.

### Frameworks and Libraries

- [Bootstrap:](https://getbootstrap.com/) Bootstrap CSS Framework used for styling and to build responsive web pages;
- [Cloudinary:](https://cloudinary.com/) Used to store all blog images and uploaded images;
- [Django:](https://www.djangoproject.com/) Main Python framework used in the development;
- [Django Allauth:](https://django-allauth.readthedocs.io/en/latest/index.html) Used for authentication and account registration;
- [Django Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/) Used to simplify the rendering of Django forms.
- [Gunicorn:](https://gunicorn.org/) Python HTTP server, used as the Web Server to run Django on Heroku;
- [Summernote:](https://github.com/summernote/django-summernote) To provide a WYSIWYG editor for customizing new blog content and add images.

### Software and Web Applications

- [Code Institute Postgres database](https://dbs.ci-dbs.net) was the Database used for this application.
- [Chrome DevTools:](https://developer.chrome.com/docs/devtools/) Used to test the response on different screen sizes, debugging and to generate a Lighthouse report to analyze.
- [PEP8](http://pep8online.com/) was used to check the code for PEP8 requirements.
- [HTML Validator:](https://validator.w3.org/) Check your code for HTML validation.
- [JSHint:](https://jshint.com/) Check code for JavaScript validation.
- [W3 CSS Validator:](https://jigsaw.w3.org/css-validator/) Check your code for CSS validation.
- [Code Beautify - Python Beautifier](https://codebeautify.org/python-formatter-beautifier) was used to format the code.
- [Heroku: Cloud Application Platform](https://dashboard.heroku.com/apps) was used for the deployment.
- [Git](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) was used as the repository for the project after being pushed from Git.
- [VSCode](https://code.visualstudio.com/) was used as the primary local Integrated Development Environment (IDE) for coding and development.
- [Lucidchart](https://www.lucidchart.com/pages/) was used to create a draft flowchart during the planning process.
- [ImgBB](https://imgbb.com/) was used to upload images and extract the source code.
- [Am I Responsive?](http://ami.responsivedesign.is) was used to generate the mockup of the website.
- [Table Convert](https://tableconvert.com/) was used to generate tables for the TESTING.md file.
- [ChatGPT](https://chat.openai.com/) was used as helpful tool during the debugging process.

## Modules imported

TO BE ADDED

## Testing

Testing information can be found in [TESTING.md file](TESTING.md).

## Deployment

Heroku was used to deploy the site. Here are the steps to deploy:

1. Log in to Heroku.
2. Click "Create a new app".
3. Choose the app name and region.
4. Click "Create app".
5. Navigate to the "settings" tab.
6. "Click "Reveal Config Vars".
7. Add a configuration variable to Heroku's Settings. The key is PORT and the value is 8000
8. Scroll down to "Buildpacks".
9. Click "Add Buildpack".
10. First, add "python" and click save.
11. Second, add "nodejs" and click save.

The live site can be found here: [Narcissistic Website](https://narcissism-website-8191a44972de.herokuapp.com/) 

### Cloning:

1. Click the "Code" button in the GitHub repository.
2. Choose "HTTPS" and copy the URL.
3. Open the Terminam (in macOS) or Git Bash (in Windows) and navigate to the repository where you would like to locate the cloned repository.
4. Type "git clone" followed by the copied URL.
5. Press enter to create the clone.

### Forking

You can fork this project and make a copy of the original repository in your own GitHub account. In this case, you can view or make changes without affecting the original. To do so:

- log into GitHub and locate the GitHub Repository;
- at the top right of the screen, click the Fork button.

It should be noted that all changes pushed to the main branch are automatically reflected on the site.

## Database creation
The database used is PostgreSQL.

### How to get started:
1. Go to https://dbs.ci-dbs.net/
2. Input email address and click Submit;
3. The Database will be created and the details emailed;
4. You will need the DATABASE_URL to connect the database to your project.

### How to connect the database to the project:
1. Create a file named **env.py** at the top level of the project;
2. Open the **.gitignore** file and add **env.py** to prevent the secret data you will add to it from being pushed to GitHub.
3. In the **env.py** file, import Python's operating system module and use it to set the value of the **DATABASE_URL** constant to the URL copied from the details emailed to you - see below:
```
import os

os.environ.setdefault(
    "DATABASE_URL", "<your-database-URL>")
```
4. Pip install the two packages required to connect to your PostgreSQL database. Then add them to the requirements file:
```
pip3 install dj-database-url~=0.5 psycopg2~=2.9
pip3 freeze --local > requirements.txt
```
5. In **settings.py** import the appropriate packages and connect the **settings.py** file to the **env.py** file:
```
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env
```
6. In the **settings.py** file, comment out the local sqlite3 database connection set up by default.

7. In the **settings.py** file, connect to the environment variable **DATABASE_URL** you previously added to the **env.py** file:
```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```
8. Your project is now connected to the database and you can create database tables with Django's **migrate** command.

## Credits

### Content

TO BE ADDED


### Code

The code was mainly based on Code Institute's walkthrough TO BE ADDED

### Acknowledgment

I am grateful to my mentor Brian Macharia for his suggestions and to my classmate Niclas for his precious support. A special thanks goes to the amazing tool that is ChatGPT: it helped me with the debugging process and whenever I got stuck.
