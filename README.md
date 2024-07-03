# The Boardgames Shelf

Developer: Stefania Frustagli

## App Overview

Welcome to my board game marketplace! This e-commerce platform is designed to connect board game enthusiasts looking to buy and sell used board games. Whether you’re clearing out your collection or searching for that rare gem, this site provides a user-friendly experience to meet your needs.

Sellers can list their board games, complete with details and images, and specify their location, making it easier for buyers to find games available nearby. My goal is to foster a community of gamers who can trade, sell, and discover new games with ease. 

#### Type of App: E-Commerce

The app functions as an e-commerce platform where users can list and sell their second-hand board games. Each transaction involves a single payment for the purchased game.

- **Business to Consumer (B2C)**: The app facilitates transactions directly between board game sellers (users) and buyers (customers).
UPDATE: Currently, all transactions are managed by a super user using Stripe, and the proceeds are manually sent to sellers after the transaction. This is a temporary solution. The goal is to transition to a fully automated transaction system in the future, allowing direct transactions between board game sellers and buyers.

- **Product Type**: Physical product - users sell their own board games.

- **Payment Model**: Single payment for each board game sold.

### Why The Boardgame Shelf?

The idea for this application stemmed from a clear gap in the market. There isn’t a dedicated, comprehensive website where board game enthusiasts can easily buy and sell used board games while managing their collections. Current platforms are fragmented and often lack the specific features needed by the board gaming community. By creating this e-commerce site, I aim to provide a centralised solution. 

My long term plan is to enable users to:
- Sell Used Board Games: list pre-owned games for sale;
- Discover Nearby Sellers: find games from sellers in a certain area;
- Catalogue Collections: in future updates, users will be able to create and manage databases of the games they own, want to sell, wish to buy, and have played;
- Review and Share: write reviews and share the gaming experiences with the community.

I would like to create a vibrant marketplace and community for board game lovers, making it easier to buy, sell, and manage board games in one place.

View the live project [here](https://the-boardgame-shelf-e0153506acf8.herokuapp.com/).

## Table of Contents 

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

### Problem Statement

I've noticed that among board gamers, 'fanatic' collecting is common, and buying games is almost a compulsive act. It's also common for them to get rid of games they don't play anymore. Instead of using eBay, I wanted to create a specific place for buying and selling second-hand games and to create a library of board games. There isn’t a dedicated, comprehensive website where board game enthusiasts can easily buy and sell used board games while managing their collections. Current platforms are fragmented and often lack the specific features needed by the board gaming community.

**Proposed solution**: 
With the creation of this platform, I aim to fill this gap and provide a centralized solution. 

### Business Organization
The business organization concerning sales is currently in its draft stages and not fully defined yet. One model could be to operate similarly to eBay, initially taking a percentage of each sale. In the future, I may explore implementing a subscription-based mechanism.

**Rationale**
This decision to adopt a commission-based model akin to eBay reflects a practical approach I would like to adopt, aimed at  generating revenue from transactions while providing value to my users. This model could allow me to ensure sustainability as I grow. As I evolve, I may explore additional monetization strategies, such as subscription services, to offer enhanced features and benefits to the community of board game enthusiasts.

#### Business goal

My goal is to create a portal where board game players can sell their second-hand games and - this will be a future feature - manage their collections within a comprehensive database. Creating an intuitive, user-friendly, and visually appealing app is the primary objective.

#### Strategies
Some of the marketing strategies I plan to implement include:

- **Search Engine Optimization (SEO)**: Optimizing the website content to rank higher in search engine results for relevant keywords.

- **Content Marketing and Social Media Marketing**: Creating compelling online content on Instagram, Facebook, and TikTok. This includes engaging posts about games, captivating images of board games, coverage of conventions, and highlights of second-hand games available on the website.

- **Design**: Emphasizing a visually appealing and functional design to enhance user experience.

- **Social Media Marketing**: Focusing on organic growth strategies to build a community of board game enthusiasts.

- **Email Marketing**: Utilizing email campaigns to inform users about new second-hand games available for sale and other updates.

- **Collaborations and Affiliate Marketing**: Partnering with board game creators and exploring affiliate marketing opportunities to expand outreach and user engagement.

#### Initial Budget
In the beginning, I'll use low-cost marketing strategies. If things go well, I might invest more to grow the business into something bigger.

#### Name Process
Choosing the right name was pretty tricky, and I considered a bunch of options like "Board Games Bazaar" and "The Board Games Vault." After doing some online research, I decided to go with "The Boardgame Shelf" since it seemed unique and there weren’t any other websites with that name.

### SEO Implementations

SEO enhancements included in the projects to improve search engine visibility and indexing include **SEO Keywords**,  **Sitemap** and **Robots.txt**.

#### SEO Keywords

To optimize the website for search engines, common keywords related to board games were researched and utilized. I brainstormed several words with the intent to ensure that board game enthusiasts can find the website. The common words were identified using Google search engine results.

The initial list of keywords included:

Board game geek,
Board game arena,
Board games bazaar,
Board games market,
Board game catalogue,
Sell your board games,
Used board games,
Buy board games,
Popular board games,
Board games geek,
Second-hand board games,
Sell your own game,
Best way to sell board games in UK,
Board game store near me,
BGG marketplace,
Virtual flea board games market,
Board game arena

Keywords were then selected based on their relevance and potential to attract board game enthusiasts. Even if some keywords were not strictly relevant, I decided to keep them to ensure maximum visibility.

**Final Keyword List**: 

- Boardgame marketplace
- Board game shelf
- Board game shop near me
- Board game geek
- Board games market
- Second-hand board games
- Sell board games
- Used board games
- Buy board games

I think that these keywords cover a broad range of relevant search terms to ensure the site is visible to users searching for board games online.

#### Sitemap
A sitemap.xml file has been added to the project. The sitemap helps search engines better understand the structure of your site and ensures that all important pages are indexed. It is automatically generated and includes all relevant URLs of the Django application.

#### Robots.txt
A robots.txt file has also been added to guide search engines on how to crawl the site. This file specifies which parts of the site should be crawled and which should not, helping to manage the load on the server and prevent sensitive or irrelevant pages from being indexed.

The robots.txt file includes the following rules:

    User-agent: *
    Disallow: /accounts/
    Disallow: /bag/
    Sitemap: https://the-boardgame-shelf-e0153506acf8.herokuapp.com/sitemap.xml


### Marketing Strategy 
Even though the website can be used by anyone who wants to sell board games, I have a specific market in mind: those who have large collections of board games, stay up-to-date with new releases and buy games compulsively. As a regular member at various board game clubs, I know that dedicated board game players and collectors currently lack a decent place to sell and buy second-hand games, apart from Facebook groups and few other choices, not really that appealing. Moreover, they don’t have a platform to share and update their collections. My goal here is to create a platform similar to Goodreads/Anobii, but with board games, and attract all the board games enthusiasts.

To start, I will focus on organic social media marketing, creating Social Media Accounts:
- I will open Instagram, Facebook, and TikTok accounts to advertise the website;
- I will start following all the board game pages I know.

#### Users and relevant platforms

My ideal users would mainly be ‘nerds’ and geeky individuals, spanning various age groups, who may use different social media platforms. Based on my experience and observations, marketing the website on Instagram, Facebook, and TikTok will effectively reach them.

I have categorized the age groups as follows:

**Age Group (45-60 years)**:
- Primarily use Facebook.
- Strategy: Engage with Facebook groups and pages dedicated to board games.

**Age Group (25-35 years)**:
- Prefer Instagram. Facebook can be used as well.
- Strategy: Use visually appealing content on Instagram and Facebook.

**Age Group (25-35 years)**:
- Prefer Instagram and TikTok.
- Strategy: Create engaging short-form videos on TikTok to attract this demographic.

By focusing my marketing efforts on these platforms and considering user behaviors, I aim to create a vibrant community of board game enthusiasts.

#### Possible ideas tailored to each platform:

1. **Instagram:**
   - Showcasing high-quality images of popular board games along with brief descriptions and prices;
   - Creating carousel posts featuring before-and-after images of well-loved board games being sold on the platform, highlighting the value of buying second-hand;
   - Sharing user-generated content by reposting photos of customers enjoying board games purchased from the website. Encouraging users to tag the account and use a specific hashtag to be featured;
   - Utilising Instagram Stories to announce new arrivals and share behind-the-scenes glimpses of the business;
   - Collaborating with board game influencers or creators to reach a wider audience and gain credibility within the community.

2. **Facebook:**
   - Sharing informative and engaging blog posts or articles related to board games, such as "Top 10 Board Games to Play This Summer" or "How to Host the Ultimate Game Night";
   - Hosting live Q&A sessions or virtual game nights where followers can interact with me/the team, discussing our favorite board games;
   - Creating polls or quizzes related to board games to encourage interaction and foster a sense of community among your followers.

3. **TikTok:**
   - Creating short and catchy videos showcasing the process of listing a board game for sale on your website, including features like photos, descriptions, and pricing.
   - Filming quick tutorials or tips on how to play popular board games, adding a link to the website where users can find those games for sale;
   - Jumping on trending challenges or hashtags on TikTok and incorporate them into your content in a creative way that relates to board games;
   - Collaborating with board game influencers or creators to reach a wider audience.


### The design process

The design aimed to be simple and reminiscent of a shelf, so I decided to utilise variations of brown to achieve this aesthetic. I think this choice of colors helps create a warm and inviting atmosphere, reminiscent of a classic game shelf.

To enhance the visual appeal of the website, I used AI to generate several potential images that could create the right atmosphere. At the end, I opted for this image:

![Background image](https://i.ibb.co/VpfqcD9/boardgameshelf-betterquality.jpg)


The image shows a massive shelf packed with tons of board games. It sets a cool, suggestive vibe, making you feel like you're stepping into a different fantasy world. It gives off strong fantasy vibes and fits perfectly as the background for both the homepage and the about page, making the whole experience more immersive for visitors.

### Colour palettes

![Colour Palette](https://i.ibb.co/5FBw0Xr/my-screenshots-2024-06-29-at-18-39-17.png)

This was created with [Coolors](https://coolors.co/).

### Fonts

The font used is called *Poppins* and it was imported using Google fonts.

### Wireframes

**Homepage** [Desktop and mobile]:

![Wireframe created using Balsamiq - Homepage on Desktop](https://i.ibb.co/LgY3Tb8/my-screenshots-2024-05-13-at-22-05-39.png)

![Wireframe created using Balsamiq - Homepage on Mobile](https://i.ibb.co/4Tj1tdN/my-screenshots-2024-05-13-at-22-05-28.png)
  
**Basket page** [Desktop and mobile]:

![Wireframe created using Balsamiq - Basket page template for desktop](https://i.ibb.co/hsPwrcX/my-screenshots-2024-05-13-at-22-06-11.png)

![Wireframe created using Balsamiq - Basket page template for mobile](https://i.ibb.co/q00vPqF/my-screenshots-2024-05-13-at-22-05-58.png)

**User Account page** [Desktop and mobile]:

![Wireframe created using Balsamiq - User Account page on desktop](https://i.ibb.co/rbhX9s6/my-screenshots-2024-05-13-at-22-05-19.png)

![Wireframe created using Balsamiq - User Account page on mobile](https://i.ibb.co/pPztmXN/my-screenshots-2024-05-13-at-22-05-06.png)

**Board game description page** [Desktop and mobile]:

![Wireframe created using Balsamiq - User Account page on desktop](media/game_description_desktop.png)

![Wireframe created using Balsamiq - User Account page on mobile](https://i.ibb.co/sqsjyx7/my-screenshots-2024-05-15-at-18-12-30.png)

### Data Model 

The structure of our database was illustrated using an Entity-Relationship Diagram (ERD). This diagram shows how different entities within the system are related to each other and helps in understanding the data flow. 

**Entity-relationship diagrams (ERD)**

First draft (in the planning process):

![ERD](https://i.ibb.co/3cMYNdK/my-screenshots-2024-05-17-at-09-40-10.png)


**Models** for the first draft:

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

![draft flowchart to organise apps](https://i.ibb.co/xY8bHPs/my-screenshots-2024-05-17-at-09-08-56.png)


**Current flowchart for apps organisation** 

The project is organized into several Django applications, trying to keep functionalities tidy and separated. As this is my second project with Django, I have decided to follow a similar structure to the one used in Boutique Ado walkthrough with Code Institute. 

The **applications** used are:

- Main app: **board_gamers_vault**

  This is the main application of the project, responsible for:
  - Project-level settings
  - URL routing
  - Global templates
  - Static files

- **Home**

  This application manages the homepage, the About page and other static content pages, providing users with information about the platform, including contact information, about us, and other informational sections. This will be further developped in the future. 

- **Marketplace**

  The Marketplace application handles all functionalities related to the e-commerce store, including:

  - Models for games
  - User profiles
  - Seller accounts
  - Basket items
  
  This is where users can browse, search, and purchase board games. Sellers can manage their products, and all e-commerce-related operations are conducted here.

- **Bag**

    The Bag application manages the shopping cart functionality, allowing users to add, remove, and view items they intend to purchase.

- **Checkout**

  The Checkout application handles the order processing, payment, and order confirmation. It ensures a smooth transaction experience for users completing their purchases.

- **Profiles**

  The Profiles application is responsible for user authentication and profile management. It includes functionalities for:

  - User registration
  - User login/logout
  - Profile editing
  - Viewing order history
  - Other user-related activities


## User Experience

#### Ideal users: 

- Board Game Shopper: 
  
  A board game enthusiast looking to expand their collection with pre-owned games or find rare and out-of-print titles. This user values affordability and the opportunity to discover unique games from other collectors.
  Needs:
  - A wide selection of pre-owned board games.
  - Detailed product information including price, condition, and images.
  - Trustworthy seller information to ensure secure transactions.
  - Convenient search and filter options to easily find specific games.
  - An easy-to-use shopping cart and checkout process.
  - Order confirmation and tracking capabilities.
  Options to save favorite games and receive notifications on game availability.

- Board Game Seller

  A board game collector or enthusiast looking to downsize their collection, make room for new games, or simply pass on games they no longer play. This user values a straightforward and efficient platform to list and sell their games.
  
  Needs:
  - An intuitive interface for listing and managing board games for sale.
  - Tools to add detailed descriptions, prices, and images of the games.
  - Visibility to potential buyers, including search optimization.
  - Easy communication with buyers to arrange sales and handle inquiries.
  - Features to update, edit, or remove listings as needed.
  - Sales management tools to keep track of inventory and transactions.

- Board Game Collector (more suitable with future features)
  
  An avid board game collector who likes to keep track of their collection, wishlist, and games they've played. This user appreciates a platform that helps them organize and showcase their collection.
  
  Needs:
  - A personalized database to catalogue owned games, games for sale, and games on their wishlist.
  - The ability to mark and review games they've played.
  - Options to make their collection public or private.
  - Social features to connect with other collectors and share reviews and recommendations.

- Casual Board Gamer
  
  Someone who enjoys playing board games occasionally and is looking for specific titles to enhance their game nights. This user prefers a simple, hassle-free buying experience.
  
  Needs:
  - Easy navigation and search functionality to quickly find games.
  - Clear and concise product information.
  - Affordable pricing and options for gently used games.
  - An uncomplicated checkout process.
  - Reliable delivery.

#### As a developer, I expect:

- User-Centric Design:
  - To focus on creating intuitive, accessible, and visually appealing interfaces that enhance user engagement and satisfaction.  
  - To create a user feedback mechanisms to gather insights and make data-driven improvements to the platform.
- Performance and Security:
  - To adhere to security best practices to protect user data and prevent vulnerabilities, maintaining user trust.

### Agile Development

The development process for this project followed Agile methodology, emphasizing continuous improvement throughout the development lifecycle.

**Project Management**: I utilised GitHub Project boards to manage tasks, user stories, and project progression effectively.

**User Stories**: User stories were categorized in a Kanban Board into EPICs A, B, C, D, E, and F based on user types and content specificity. I prioritized user stories using the MoSCoW method, which categorizes requirements into Must have, Should have, Could have, and Won't have categories based on their importance and urgency.

[Link to the GitHub Project board](https://github.com/users/StefFrustagli/projects/3/views/1)

**Continuous Improvement**: Despite working solo on this project, I actively sought ways to enhance development processes and product quality. Regular retrospectives allowed me to reflect on past work, pinpoint areas for improvement, and brainstorm solutions.

### User Stories

**[EPIC A] View and navigation**

A1 - As a board games shopper, I want to be able to view a list of products available to purchase so that I can select the ones I want.

A2 - As a board games shopper, I want to be able to view individual product details so that I can identify the price, description, product condition and product image.

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

### Functionalities Overview
The app is currently in its early stages of development, with several functionalities yet to be implemented.

Mainly it operates as a marketplace where registered users can buy and sell second-hand board games. Users can view available games, make purchases, and list their own games for sale.

#### Payment Handling
Currently, payments are processed using **Stripe** by the superuser (myself). Upon a game being sold, money is received into the Stripe account and then transferred to the seller within 2 working days. Sellers are notified via email when a game is sold, along with instructions to facilitate payment retrieval. Similarly, buyers receive a confirmation email containing the order number and relevant contact information in case they encounter any issues.

Please note that this payment handling is a temporary solution. I am actively working on implementing a more automated system to handle multiple payments seamlessly.

    To test the checkout process use the Stripe test card details:

    Card number: 4242424242424242
    CVC: Any 3 digits
    Expiry: Any future date (eg. 04/25)

#### Delivery and Shipping cost

Shipping costs are currently handled by sellers and are included in the product price, so they are not calculated separately. At the moment, all transactions are conducted in British Pounds (GBP), as the market is primarily focused on the UK.

### Current Features

#### Homepage

![Homepage](https://i.ibb.co/BjKyxz6/my-screenshots-2024-07-02-at-08-28-52.png)

On the homepage, users can quickly understand the website's purpose. At the top, there is a navbar featuring the website name on the left, a search bar in the center, and two icons on the right: "My Account" and "Shopping Basket". Below there is a mini banner saying "Sell and buy pre-owned board games".  In the middle of the screen, there are two prominent buttons that allow users to access the main actions of the website. These buttons are designed to guide users towards the most important features or sections. At the bottom, the footer contains various information related to the website, including contact details, legal information, and links to social media. Additionally, there is a newsletter subscription form for users who want to stay updated with the latest news and updates.

The navbar, mini banner and footer are consistently displayed across all pages of the website.

You can see the details of the homepage sections below:

##### Navbar

![Website navbar](https://i.ibb.co/X8NZKc5/my-screenshots-2024-07-02-at-08-30-40.png)

The navbar features:

- **Website name**:  located on the left side of the navbar, clicking on it returns users to the homepage, providing easy navigation back to the main page of the website.

- **Search bar**: positioned in the center of the navbar, the search bar enables users to quickly search for specific items, content, or information within the website. It enhances user experience by allowing for efficient navigation and discovery of desired content.

- **My Account**: this icon functions as a dropdown menu. For users who are not logged in, it offers options to "Login" or "Register". Once logged in, users see additional options such as "Logout", "My Profile", and "Boardgame Management". "My Profile" allows users to view and update their personal information, while "Boardgame Management" provides tools to manage their boardgame collection or listings.

  The dropdown menu for not-logged-in users: 

  ![My account dropdown menu for not-logged-in users](https://i.ibb.co/56j3YXj/my-screenshots-2024-07-02-at-15-27-31.png)

  The dropdown menu for logged-in users:

  ![My account dropdown menu for logged-in users](https://i.ibb.co/QFwVw10/my-screenshots-2024-07-02-at-17-18-11.png)



- **Shopping Basket**: this icon indicates the user's shopping basket, allowing them to view and manage items they have added for purchase.

  The shopping basket with items inside appears like this:

    ![Shopping basket with items](https://i.ibb.co/dWdmd8z/my-screenshots-2024-07-02-at-17-21-56.png)

At the bottom of the navbar, we can find the following dropdown menus and the About page link:
    ![Dropdown menus and about page link](https://i.ibb.co/PN1RCmS/my-screenshots-2024-07-02-at-17-25-16.png)

- **On Sale**: This category allows users to filter and view games that are currently discounted or part of special promotions. It's perfect for users looking for great deals and limited-time offers.

- **Category**: This filter enables users to browse games based on specific board games types, such as Storytelling, Strategy, Placement, and more. It helps users quickly find games that match their interests and preferences.

- **Condition**: This filter lets users sort games based on their condition, such as new, used, or refurbished. It provides flexibility for users who may be looking for budget-friendly options or collector's items.

- **About the Team**: This link redirects users to the "About" page, where they can find detailed information about the website and the team behind it. It includes a welcome message and a feedback form for users to leave their comments and suggestions.

##### Mini banner

![Mini banner](https://i.ibb.co/m4PNG2d/my-screenshots-2024-07-02-at-08-31-04.png)

##### Homepage banner with two buttons
In the middle of the page, a white banner appears with two buttons that allow to the two main pages of the website.

![Homepage banner](https://i.ibb.co/gwh7Mtr/my-screenshots-2024-07-02-at-08-59-10.png)


#### Footer
![Footer](https://i.ibb.co/qp0LxWN/my-screenshots-2024-07-01-at-15-52-59.png)

The footer appears on every page of the application and includes essential information such as the app name, a brief description, social media links, a contact us section with an email link, a Privacy Policy link, and a Mailchimp subscription form for the newsletter.


##### GDPR
The Privacy Policy is displayed within the footer on every page of the application.

[Privacy Policy](https://www.termsfeed.com/live/2cfed02a-973b-42ae-a51c-23056d8b23e8)


### "Board games on sale" Page

![Board games on sale Page](https://i.ibb.co/bRhdmYm/my-screenshots-2024-07-02-at-09-13-47.png)

It displays the list of available games with all the relevant infomation.

Details diplayed with every game:

![Details of game](https://i.ibb.co/T2ykmfY/my-screenshots-2024-07-02-at-13-21-44.png)

Sellers can only edit and delete their own games. They will see the "Edit" and "Delete" options for their listed games.

Other elements in the page:
- **Toggle Arrow Up**: Positioned at the bottom of the page, the toggle arrow up icon serves as a quick navigation tool for users to scroll back to the top of the page with a single click. It enhances user experience by providing a convenient way to navigate long pages without manual scrolling. ![Toggle Arrow Up](https://i.ibb.co/5vnHRnN/my-screenshots-2024-07-02-at-13-33-17.png)


- **Display of Games** and **"Sort by" Bar**: This section of the website displays a collection of games, likely in a grid or list format, showcasing various titles, images, and possibly brief descriptions. Alongside or above this display, the "Sort by" bar offers users options to organize and filter the displayed games according to preferences such as price, popularity, release date, or genre. It provides users with flexibility and control over how they explore and browse the available games, ensuring a tailored browsing experience.
![Display of Games and Sort by Bar](https://i.ibb.co/DGNd5HY/my-screenshots-2024-07-02-at-13-21-32.png)

### "Boardgames Management" Page

The "Sell Your Game" button redirects users to the "Boardgames Management" page. This page is also accessible via the "My Account" dropdown menu. The "Boardgames Management" page allows users to list their board games for sale, which will then appear in the "Board Games on Sale" list. To add a game, users need to provide the following information:

- Title: the name of the board game.
- Price: the selling price of the game.
- Availability: availability status of the game.
- Condition: the condition of the game (e.g., new, used, refurbished).
- Category: game genre.
- Description: a description of the game.

![Sell your game Page - part 1](https://i.ibb.co/GtQgXGP/my-screenshots-2024-07-02-at-13-38-57.png)

- Seller's Message: An optional message from the seller, providing additional information or personal notes about the game.
- Image.

![Sell your game Page - part 2](https://i.ibb.co/r0MJM99/my-screenshots-2024-07-02-at-13-39-07.png)

This streamlined process ensures that sellers can easily and effectively manage their listings, making their games available to potential buyers on the platform.

### "About" Page

On the "About" page, users can find information about the website and the team. The page includes a welcome message and a feedback form for users to easily leave their feedback.

![Welcome message](https://i.ibb.co/cwcj7J3/my-screenshots-2024-07-02-at-10-39-30.png)

![Feedback Form](https://i.ibb.co/m9n22cQ/my-screenshots-2024-07-02-at-10-39-43.png)

### "Shopping Bag" Page

![Shopping bag page](https://i.ibb.co/4T4L3Hs/my-screenshots-2024-07-02-at-15-12-30.png)

In the shopping bag, buyers can view the products they intend to purchase along with all the relevant information.
The product can be removed from the basket by clicking on "Remove". Clicking on Secure checkout, they can proceed with the purchase.

### "Checkout page" Page

![Checkout page part 1](https://i.ibb.co/LPQSVsN/my-screenshots-2024-07-03-at-06-20-30.png)
![Checkout page part 2](https://i.ibb.co/93Z4McC/my-screenshots-2024-07-03-at-06-20-46.png)
![Checkout page part 3](https://i.ibb.co/yhCTLzS/my-screenshots-2024-07-03-at-06-20-53.png)

The checkout page provides a seamless and secure process for completing purchases. Buyers can review their order details, enter card details information, and make payments through the secure payment gateway. Currently, all transactions are managed using Stripe.

When a game has been purchased, it will disappear from the "Board Games on Sale" page.

### "My profile" Page

![My profile page](https://i.ibb.co/kXz9KRg/my-screenshots-2024-07-02-at-15-22-13.png)


In "My Profile," users can access and customize some of their personal information (this feature will be improved in the future), as well as view their order history.

#### Authentication and notification messages

In the navigation bar, where the shopping cart is, notifications, such as sign out, edits and deletions, will appear.

Examples of messages:

!["Added to the shopping bag" message](https://i.ibb.co/x2MD6dm/my-screenshots-2024-07-02-at-17-21-50.png)

!["Successfully signed in" message](https://i.ibb.co/KG1Ky0N/my-screenshots-2024-07-02-at-17-17-58.png)

#### Registration page
The Registration page, which is visible to non-logged-in users, presents a registration form. The mandatory fields are 'Username' and 'Password' (to be entered twice), while the optional field is 'Email' address.

![Register page](https://i.ibb.co/j44QBXm/my-screenshots-2024-07-02-at-15-27-42.png)

In addition, it contains a link that leads to the Login page, if the user has already created an account.  

#### Sign in page
The Sign in page allows registered users to sign into their account by entering their username and password. It also contains a link to the Register page, if the user hasn't created an account yet.

![Sign-in form](https://i.ibb.co/0q7YCH3/my-screenshots-2024-07-02-at-15-27-51.png)

Also, users have the option of having their login information remembered, so they don't have to re-enter their login details each time they visit the website.

#### Logout page
The logout page allows users to log out of their accounts. The user must confirm their choice. They  can also cancel the action and return to the homepage.

![Log out form](https://i.ibb.co/7JkySHr/my-screenshots-2024-07-02-at-17-54-27.png)

#### Password Reset

![Password reset](https://i.ibb.co/FhLjP47/my-screenshots-2024-07-02-at-15-27-59.png)


#### Django admin board
The admin board allows administrators to control the website. They can add topics and contents, edit the About section and authorise comments to be published.

![Django Administrator Board](https://i.ibb.co/tBMsMBW/my-screenshots-2024-07-02-at-10-45-41.png)

In the admin board, it is also possible to control users' permissions, deactivate their accounts or make them admin users.

The functionalities are still basic and will be improved in the future.

#### Favicon
The favicon was generated using [Microsoft Designer](https://designer.microsoft.com/image-creator). It features an image of a wizard about to cast a spell in front of a suitcase containing a book and various dice, surrounded by numerous objects and artifacts.

![Favicon](https://i.ibb.co/71tpgxz/wizard-logo.jpg)

It was converted to a favicon using [favicon.io](https://favicon.io/favicon-converter/)

#### Error pages
The error pages simply provide the user with a link back to the homepage and inform them what type of error they encountered.

#### Social media currently set up

A Facebook page has been created for the application. This page will be used to share updates, engage with the community, and provide support to users.

![Facebook page 1](https://i.ibb.co/MGPr5dW/fb1.png)

![Facebook page 2](https://i.ibb.co/HHCSQ2w/fb2.png)

![Facebook page 3](https://i.ibb.co/dW6qvg5/fb3.png)

Find the FB page [here](https://www.facebook.com/profile.php?id=61561423170621).

#### Mailchimp Newsletter

To keep my users informed and engaged, I have set up a [Mailchimp](https://mailchimp.com/?_ga=2.244262146.682070205.1719697033-1477901815.1719697032&currency=GBP) newsletter. Subscribers will receive regular updates on new game listings, special promotions, and the latest developments in the app. This ensures that our community stays connected and always knows what's happening.

The Mailchimp form is located in the footer and appears like this:

![Mailchimp](https://i.ibb.co/b3jDMtv/my-screenshots-2024-06-29-at-22-50-47.png)


### Future Features and general aspects left to implement
Having an ambitious plan for the app, I intend to expand its capabilities in many ways. 

First of all, in order to make the website professional and appealing, many aspects of the graphic will be improved. This current version should be considered a first draft, with much work still to be done.

Future updates will focus on enabling users to customize their profiles and showcase their game collections to other players.

Specifically, upcoming features will include personalized profiles where users can catalogue their collections, track their wish lists, log played games, and share reviews.

The payment handling process will be improved and automated in the future.

## Technologies used

### Programming Languages

- Programming languages used in this project are **HTML5**, **CSS3**, **JavaSctipt** and **Python**.

### Frameworks and Libraries

- [Bootstrap:](https://getbootstrap.com/) Bootstrap CSS Framework used for styling and to build responsive web pages;
- [Django:](https://www.djangoproject.com/) Main Python framework used in the development;
- [Django Allauth:](https://django-allauth.readthedocs.io/en/latest/index.html) Used for authentication and account registration;
- [Django Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/) Used to simplify the rendering of Django forms.
- [Gunicorn:](https://gunicorn.org/) Python HTTP server, used as the Web Server to run Django on Heroku;
- [Summernote](https://github.com/summernote/django-summernote) was used to provide a WYSIWYG editor for customizing new blog content and add images.
- [Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to simplify form rendering.

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
- [Microsoft Designer](https://designer.microsoft.com/image-creator) was used to create images for the project.
- [Favicon.io](https://favicon.io/favicon-converter/) was used to convert the chosen image into the favicon.
- [Mailchimp](https://mailchimp.com) was used to set up the subscription newsletter.
- [Amazon S3](https://aws.amazon.com/s3/) was used to store static files and images.
- [Stripe](https://js.stripe.com/v3/) was used for secure payments (referenced in base.html).
- [Sitemaps](https://www.xml-sitemaps.com/) was used for the Sitemap.

## Modules imported

1. **Django Modules:**
   - `from django.conf import settings`
   - `from django.http import HttpResponse`
   - `from django.views.decorators.http import require_POST`
   - `from django.views.decorators.csrf import csrf_exempt`
   - `from django.core.mail.backends.smtp import EmailBackend`
   - `from django.contrib import admin`
   - `from django.shortcuts import render, get_object_or_404`
   - `from django.contrib import messages`
   - `from django.contrib.auth.decorators import login_required`
   - `from django.db import models`
   - `from django.db.models.signals import post_save`
   - `from django.dispatch import receiver`
   - `from django.urls import path`
   - `from django.forms.widgets import ClearableFileInput`
   - `from django.utils.translation import gettext_lazy as _`
   - `from django import forms`
   - `from django.apps import AppConfig`

2. **Django Custom Imports:**
   - `from .models import FeedbackRequest, About, Category, Game, SellerProfile, UserProfile`
   - `from .widgets import CustomClearableFileInput`
   - `from .forms import UserProfileForm, FeedbackRequest`
   - `from . import views`
   - `from checkout.models import Order`
   - `from checkout.webhook_handler import StripeWH_Handler`

3. **Third-Party Libraries:**
   - `import stripe`
   - `import smtplib`
   - `import ssl`

4. **Standard Python Modules:**
   - `import os`
   - `import sys`
   - `from django.utils.crypto import get_random_string`


## Testing

Testing information can be found in [TESTING.md file](TESTING.md).

## Deployment

**Heroku** was used to deploy the site. Here are the steps to deploy:

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

The live site can be found here: [The Boardgame Shelf](https://the-boardgame-shelf-e0153506acf8.herokuapp.com/).

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

### AWS Configuration

Amazon Web Services S3 were used to store static files and images.

Configuration:

- Log on to AWS account on aws.amazon.com and create an account if necessary.
- From the dashboard access the S3 services.
- Create a new 'bucket', it is recommended to give this a name similar to your application to make it easy to remember and use, choose a region close to you, uncheck "Block all public access" and acknowledge that the bucket will be public.  
Next, click on the new bucket to configure it.
- Go to the properties tab and turn on static website hosting, fill in default values for index and error document settings - e.g. index.html and error.html and click on Save.
- Go to the permissions tab and make 3 changes to configure the bucket :

    - Step 1 Configure CORS : 
        - Paste the following CORS configuration string :
    	[ { "AllowedHeaders": ["Authorization"],
                "AllowedMethods": ["GET"],
                "AllowedOrigins": ["*"],
                "ExposeHeaders": [] } ]

    - Step 2 Generate Policy:
        - Go to the bucket policy area, click on Edit and click on policy generator.  
        - Choose S3 bucket policy from drop-down
	    - Put asterisk in Principal field
	    - Select get object from Actions drop-down
	    - Copy ARN and paste into ARN box on the policy generator page
	    - Click Add Statement
	    - Click Generate Policy then copy the policy into the policy editor window
        - Add /* to the end of the Resource key
	    - Click Save

    - Step 3 ACL :
        - Go to the Access Control List area
		- Set the list objects permission for everyone under the Public Access section and
		check the box to confirm you want this permission setting

- Create a user to access the bucket through IAM as follows :
    - Return to the services menu on the dashboard and access the IAM area
    - Create a group
    - On the same page click on Policies, then Create Policy, go to JSON table and select Import Managed Policy
    - Click on Import managed policy on rhs
	- Search for S3 and select AmazonS3FullAccess and click on Import
	- Go back and get the Bucket Policy ARN (generated when bucket was created)
	- Change the Resource value from * to ARN bucket and its contents - e.g : 
        "Resource": [
                    "arn:aws:s3:::pf5-iomha-prints",  (sensitive)<br>
                    "arn:aws:s3:::pf5-iomha-prints/*"
                ]
	- Click Next and then Review Policy
	- Give the policy a name and click Create Policy
    - Attach the policy to the group you created as follows : Go to groups, click on your group, go to the Permissions tab, click Add permissions and select Attach policies, select the policy created on previous step and click Attach permissions
    - Create user to put into the group. Click Users on lhs, click Add User, assign name check the programmatic access checkbox, click on Next:Permissions.  Add user to group, click through to the end and click Create User.

- Download and save the generated csv which contains the users access and secret access keys
- Update the AWS section of the settings.py file - replace the bucket name and region with the values you set up in the previous steps :

			if 'USE_AWS' in os.environ:
				# Bucket Config
				AWS_STORAGE_BUCKET_NAME = 'pf5-iomha-prints'    <------ bucket name and region
				AWS_S3_REGION_NAME = 'eu-west-1'
				AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
				AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

- Add the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY config vars to heroku using the values from the downloaded cvs
- Add USE_AWS = True to the Heroku config vars
- Remove the DISABLE_COLLECTSTATIC config var at this point from Heroku
- The custom_storages.py file that is part of this project will tell Django to use S3 to store static and media files when collectstatic is run
- The remaining AWS configuration settings needed are already configured in this projects settings.py file
- Go to the S3 dashboard and create a folder called media in the new bucket.  Specify grant public-read access on the folder and tick the checkbox to confirm.

### Stripe configuration

- Log in to your Stripe account or create one if necessary.
- Add STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY to the Heroku config vars, assign these variables values from your Stripe account dashboard.
- Create a webhook endpoint for use with your applications.  On the stripe dashboard go to the Developers -> Webhooks area, click add endpoint, use the url of your Heroku application with '/checkout/wh/' tagged onto the end of the url string.  When configuring the endpoint, the events to register to listen to are payment_intent_succeeded and payment_intent_failed
- Once the endpoint is set up get the signing secret for the webhooks and save this value as a Heroku config var called STRIPE_WH_SECRET.

## Credits

### Content

- The background picture and favicon were generated using Microsoft Designer.
- Board game pictures were sourced from eBay for testing purposes.
- Board game descriptions were randomly taken from the internet to simulate what a user might use to describe their game. Some websites used were [BGG - Board Game Geek](https://boardgamegeek.com/) and Amazon UK.


### Code

The code was mainly based on Code Institute's walkthrough.

### Acknowledgment

I am grateful to my mentor Brian Macharia and to Code Institute tutors for their help with the debugging process. A special thanks goes to the amazing tool that ChatGPT is: it helped me whenever I got stuck.
