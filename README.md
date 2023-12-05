# Niall's Barbershop 
<img src="" ><br>
- [Live Site](https://niallsbarbershop-e4e7dc2878db.herokuapp.com/)
- [GitHub Repo](https://github.com/DanMorriss/nialls-barbershop)
<hr>
Introduction.
<hr>
Niall's Barbershop is a website with a booking system for a Barber Shop in Swindon, Wiltshire. 
The web application allows users to create an account, login and logout of the site.
The site was created using Django and has full CRUD functionality and an intuitive UI to make the process of booking a haircut both easy and enjoyable. 
<br><br>

## Table of contents
  * [Overview](#overview)
  * [UX](#ux)
    + [Strategy](#strategy)
    + [Scope](#scope-hr-)
    + [Structure](#structure-hr-)
    + [Skeleton](#skeleton-hr-)
    + [Surface](#surface-hr-)
      - [Color Scheme & Fonts](#color-scheme-and-fonts)
      - [Visual Effects](#visual-effects)
  * [Agile Methodology](#agile-methodology)
  * [Features](#features)
    + [Existing Features](#existing-features)
      - [Client bookints management](#client-bookings-management)
      - [Staff bookings management](#staff-bookings-management)
      - [Create bookings](#create-bookings)
      - [Menu](#menu)
      - [Information](#information)
    + [Potential Future Features](#pontential-future-features)
  * [Responsive Layout and Design](#responsive-layout-and-design)
  * [Tools Used](#tools-used)
    + [Python packages](#python-packages)
  * [Testing](#testing)
  * [Deployment](#deployment)
    + [Deploy on heroku](#deploy-on-heroku)
    + [FORK THE REPOSITORY](#fork-the-repository)
    + [CLONE THE REPOSITORY](#clone-the-repository)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Code](#code)
  * [Acknowledgements](#acknowledgements)

## Overview
Overview.

## UX
This site was created according to the Five Planes Of Website Design:<br>
### Strategy<hr>

**User Stories:** <br>

|EPIC|ID|User Story|
| :--|--|:--|
|**Authentication**| | |
| |1A| As a site user I can|
| |1B| As a site user I can|
| |1C| As a site user I can|
| |1D| As a site user I can|

**Project Goal:**<br>
To create a website with good UI and UX to promote Niall's Barbershop where potential customers can login, book and update an appointment. 

**Project Objectives:**<br>
- Create a sleek, modern website to promote Niall's Barbershop, containing all the information customers might want.
- Allow users to create an account.
- Allow users to create an appointment at a time when here are no other bookings to avoid double bookings.
- Allow users to see their upcoming and past appointments.
- Allow users to cancel or modify an existing appointment.
- Allow staff to login to an admin area.
- Allow staff to view all upcoming booked appointments.
- Allow staff to search bookings by date and username.
- Allow staff to create a booking for a customer.
- Allow staff to modify an existing booking.
- Allow staff to remove/cancel an existing appointment.
- Provide feedback to users when they have made changes.
- Send email updates to customers when a booking has been made of modified.
- Allow staff to confirm appointments from the admin panel.
- Allow users to update their password, username and email address.
- Show different site functionality to logged in members than to non logged in users.

### Scope<hr>
**Simple and Intuitive UX**<br>
- Create a website that portrays the mood and feel of the barbershop.
- Create a responsive navigation menu.
- Create a footer with social links.
- Include store location and opening times.
- Ensure that the user is visually notified of all changed to their account, eg booking conformation.
- Ensure that the user keeps their orientation throughout their website experience. 

**Relevant Content**<br>
- Make sure all the available haircut services are listed on the site.
- Display a map to the barbershop.
- Display only available time slots when booking a service.

**Responsiveness**<br>
- Create a responsive website that works on every device and screen size.<br><br>

### Structure<hr>
Introduction:

#### Navigation

#### Footer

#### Pages

##### Landing Page

The main landing page has hero image with moving, interactive logo to spark the users interest right away. 

Below the hero image is an about section giving the user some information about the barbershop.

Below the about section is some information on the different services available. Each one can be clicked on and a modal appears with more information about that service including a 'Book a Haircut' button. 

The information on the different services is taken from the database, so an admin user can update it from the django admin panel.

At the bottom of the landing page is a contact section with address, opening times and a 'Book a Haircut' button.

If the user is logged in, the 'Book a Haircut' buttons will take them to the booking form. If the user isn't logged in they are redirected to the sign in page before arriving at the booking form.

##### Sign Up Page
##### Sign In Page
##### Account Home Page
##### Admin Account Home Page
##### Booking Form
##### Update Booking Page
##### Booking Detail Page
##### Admin Booking Detail Page



#### Sitemap
The project flowcharts for the site structure was created using [LucidChart](https://www.lucidchart.com/).
<details>
<summary>Sitemap:</summary>
<img src="media/sitemap2.png"><br>
</details>

### Skeleton<hr>
**Wireframes**

The wireframes for mobile and desktop were created with [Balsamiq](https://balsamiq.com/) tool and can be viewed <details>
<summary>Here:</summary>
Homepage<br>
<img src="media/homepage-wireframe.png"><br>
Login/Logout pages<br>
<img src="media/login-logout-wireframe.png"><br>
Book a haircut<br>
<img src="media/book-a-haircut-wireframe.png"><br>
</details><br>

**Database**
The project uses ElephantSQL as PostgreSQL relational database for storing the data.
<details>
  <summary>Model</summary>
  <img src="media/database-schema2.png"><br>
</details><br>

### Surface
#### Color Scheme and Fonts

- The fonts I used for this site were imported from [Google Fonts](https://fonts.google.com/):
  - Sancreek for the headings
  - Tenor Sans for the body

<img src="media/fonts.png" width="60%">

- The colors used were based on the the colors in the logo.
  - #212529 --clr-gold
  - #af7f1f --clr-light
  - #faf8f2 --clr-dark

<img src="media/color-palette2.png" width="60%">



#### Visual Effects

* **Hover effects**<br>
<details>
  <summary>NavBar</summary>
<img src="static/images/hover.gif" width="40%"><br>
</details>
<details>
  <summary>Bootstrap standard button hover effect</summary>
<img src="static/images/buttonhover.gif" width="40%"><br>
</details>
<br>
<br>

## Agile Methodology
This project was developed using the Agile methodology.<br>
All epics and user stories implementation progress was registered using [GitHub](https://github.com/). As the user stories were accomplished, they were moved in the GitHub Kanban board from **ToDo**, to **In Progress**, **Done** and **Not Implemented** lists.
The board can be viewed [here](https://github.com/users/DanMorriss/projects/5).
<details>
<summary>Sprint Details</summary>

- **KANBAN BOARD**<br><br>
    <img src="static/images/kanban.png" width="60%"><br><br>
- **EPIC 1 - BASE SETUP**<br>
    -1A Create<br>
    <img src="static/images/epic-1.png" width="60%"><br><br>
</details><br><br>

## Features

### Existing Features and sub-pages

#### Feature 1

### Potential Future Features

## Responsive Layout and Design
How the breakpoints are set.

**Tested devices:**

- iPhone 13
- MacBook Pro
- Samsung Galaxy Z flip 5


## Tools Used

- [GitHub](https://github.com/) for hosting the source code of the program and version control
- [VS Code](https://code.visualstudio.com/) for writing and testing the code
- [Heroku](https://dashboard.heroku.com/) used for deploying the project
- [ElephantSQL](https://www.elephantsql.com/) for the PostgreSQL database
- [Balsamiq](https://balsamiq.com/wireframes/) for creating the wireframes
- [Canva](https://www.canva.com/) for creating the logo
- [LucidChart](https://www.lucidchart.com/) for creating the Flowchart and Database schema
- [Favicon.io](https://favicon.io/) for converting the sites favicon
- [Font Awesome](https://fontawesome.com/) for the site's icons
- [Bootstrap4](https://getbootstrap.com/) for the initial styling of of the site
- [Google Fonts](https://fonts.google.com/) for the typography
- [Code Institute Pylint](https://pep8ci.herokuapp.com/) for validating the python code
- [HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) for validating the HTML
- [CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) for validating the CSS
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) for debugging the project
- [W.A.V.E.](https://wave.webaim.org/) for testing accessibility
- [Cloudinary](https://cloudinary.com/) for storing static data
- [Chrome LightHouse extension](https://developer.chrome.com/docs/lighthouse/overview/) for testing performance

### Python packages

- [Django](https://www.djangoproject.com/) was used as the framework for the site.
- [Allauth](https://django-allauth.readthedocs.io/) for the login authentication.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/) for help styling the forms.
- [Cloudinary](https://cloudinary.com/) for hosting the images.
- [Gunicorn](https://gunicorn.org/) for handling the HTTP requests in production.
- [Psycopg2](https://www.psycopg.org/) for aiding communication between Django and PostgresSQL
- [Formtools](https://django-formtools.readthedocs.io/) for additional form utilities.
- [Whitenoise](http://whitenoise.evans.io/en/stable/) for deploying the static files to Heroku.

A full list of the requirements and the versions used can be found in the reqquirements.txt file. To install them and run them on your own machine first setup a virtual environment with the command to create a venv... <br>
`python3 -m venv venv` <br>
Then this command to run it... <br>
`source venv/bin/activate` <br>
To stop running the environment simply type the command... <br>
`deactivate`

## Testing
Testing

## Bugs

- Adding the searchbox to the admin panel was causing a user to not be able to view the account home page. I all code related to the search panel inside an if statement to fix the error.
- While testing I needed to create a test service as the services list is taken from the database. So, without creating one nothing cloud be valid.
- Static files were not being issued on Heroku, I needed to install and setup whitenoise.
- On deployment, the email confirmations were causing an internal server error the user. I needed to give Heroku assess to the email password.
- collectstatic needs to be run on any static changes.

## Deployment

### Deploy on Heroku
 1. Create requirements.txt file 
 
 In the terminal enter the command ` pip3 freeze > requirements.txt`, and a file with all requirements will be created. 
 
 2. Setting up Heroku

    * Go to the Heroku website (https://www.heroku.com/) 
    * Login to Heroku and choose *Create App* 
    * Click *New* and *Create a new app*
    * Choose a name and select your location
    * Go to the *Resources* tab 
    * From the Resources list select *Heroku Postgres*
    * Navigate to the *Deploy* tab
    * Click on *Connect to Github* and search for your repository
    * Navigate to the *Settings* tab
    * Reveal Config Vars and add your Cloudinary, Database URL (from Heroku-Postgres) and Secret key.    

3. Deployment on Heroku

    * Go to the Deploy tab.
    * Choose the main branch for deploying and enable automatic deployment 
    * Select manual deploy for building the App 
    
### Fork the repository
For creating a copy of the repository on your account and change it without affecting the original project, use<b>Fork</b> directly from GitHub:
- On [My Repository Page](https://github.com/), press <i>Fork</i> in the top right of the page
- A forked version of my project will appear in your repository<br></br>

### Clone the repository
For creating a clone of the repository on your local machine, use<b>Clone</b>:
- On [My Repository Page](https://github.com/), click the <i>Code</i> green button, right above the code window
- Chose from <i>HTTPS, SSH and GitClub CLI</i> format and copy (preferably <i>HTTPS</i>)
- In your <i>IDE</i> open <i>Git Bash</i>
- Enter the command <code>git clone</code> followed by the copied URL
- Your clone was created
<hr>

## Credits

### Content
All the content was created for the site by myself.

### Media
The logo was designed and created using [Canva](https://www.canva.com/en_gb/) by myself.

### Code

- Help with Bootstrap from their [documentation](https://getbootstrap.com)
- Django's docs have been invaluable:
  - [Date](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#date)
  - [Time](https://docs.python.org/3/library/time.html)
  - [Email](https://docs.djangoproject.com/en/3.2/topics/email/#email-backends)
  - [Q Objects and advanced queries](https://docs.djangoproject.com/en/3.2/topics/db/queries/#complex-queries-with-q-objects)
- Additional help with email authentication from this article on [Code Snail](https://www.codesnail.com/django-allauth-email-authentication-tutorial/)
- This article from [Stack Overflow](https://stackoverflow.com/questions/3728528/testing-email-sending-in-django) also helped with setting up email.
- The [Whitenoise Docs](https://whitenoise.readthedocs.io/en/stable/django.html)
- This link from [Stack Overflow](https://stackoverflow.com/questions/30244042/django-updateview-creates-a-new-object-instead-of-updating-the-current-object) helped when I was having issues updating a booking.
- This video by [BuyBytes](https://www.youtube.com/watch?v=8xb9s3jnRF8) of using a Form Wizard was useful, even though I didn't end up using it in the final deployment.
- This video from [Corey Schafer](https://www.youtube.com/watch?v=Kg1Yvry_Ydk) on using venv was great for understanding virtual environments.

## Acknowledgements

- Roman Rakic for his help on Slack with linking up my urls.
- Tomislav for his help understanding venv, cloudinary & how django works with static. His patience helping me understand the settings in a full stack application has been amazing.
- Precious Ijege my Code Institute mentor.
- Kent Yates for testing my application and supplying moral support.
- Selina Sheerin for her continued encouregment and keen eye for spelling and grammar mistakes. 

Make sure to remove the DISABLE_COLLECTSTATIC = 1 config var from heroku before final deployment.