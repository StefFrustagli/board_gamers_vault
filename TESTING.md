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

## User Stories completion

To check User Stories completion, please refer to the [Kanban Board]().

## Automated testing
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
The website's responsiveness has been tested using Google Chrome Developer Tools. To ensure compatibility across different devices, various screen resolutions were simulated. Custom media queries were implemented to address issues with the iPad Pro and 5K iMac Pro displays.

The website now displays responsively across a wide range of devices and screen sizes.

## Bugs resolved

- **Favicon not appearing on all pages**

There was an issue with the favicon that displayed correctly on the homepage, but failed to render on other pages. This error was caused by the incorrect paths specified in the link tags.
By incorporating ```[% static %]``` into the file paths, I made sure that the favicon files were correctly referenced, regardless of the URL.

```
<!-- Favicon -->
    <link rel="apple-touch-icon" sizes="180x180" href="{% static 'favicon/apple-touch-icon.png' %}">
    <link rel="icon" type="image/png" sizes="32x32" href="{% static 'favicon/favicon-32x32.png' %}">
    <link rel="icon" type="image/png" sizes="16x16" href="{% static 'favicon/favicon-16x16.png' %}">
    <link rel="manifest" href="{% static 'favicon/site.webmanifest' %}">
```

## Remaining bugs

There are no major issues that impact the website's functionalities. 