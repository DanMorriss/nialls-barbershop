
[GitHub Repo](https://github.com/DanMorriss/nialls-barbershop)




# Niall's Barbershop 
[Live Site](https://niallsbarbershop-e4e7dc2878db.herokuapp.com/)
<img src="" ><br>
<hr>
Introduction.
<hr>

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

|   EPIC                                |ID|                                User Story                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**Authentication**                     |  ||
|                                       |1A| As a site user I can|
|                                       |1B| As a site user I can|
|                                       |1C| As a site user I can|
|                                       |1D| As a site user I can|

**Project Goal:**<br>
Project goal.

**Project Objectives:**<br>
* Objective one

### Scope<hr>
**Simple and Intuitive UX**<br>
* Create...

**Relevant Content**<br>
* Add...

**Features for Upgraded Experience**<br>
* Create...

**Responsiveness**<br>
* Create a responsive website that works on every device and screen size.<br><br>

### Structure<hr>
Introduction:

Site structure

#### Flowchart
The project flowchart for the site structure was created using <b>LucidChart</b>.<br><br>
[![N|Solid](static/images/flow_chart.png)](static/images/flow_chart.png)<br><br>

### Skeleton<hr>
**Wireframes**<br>
The wireframes for mobile and desktop were created with [Balsamiq](https://balsamiq.com/) tool and can be viewed <details>
<summary>Here:</summary>
<img src="#"><br>
</details><br>

**Database**
The project uses ElephantSQL as PostgreSQL relational database for storing the data.

<details>
  <summary>Model</summary>
<img src="#"><br>
</details><br>

### Surface
#### Color Scheme and Fonts
* The fonts I used for this site were imported from [Google Fonts](https://fonts.google.com/):
* Font 1
* Font 2

<img src="#" width="60%">

<img src="#" width="60%">

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

* **KANBAN BOARD**<br><br>
    <img src="static/images/kanban.png" width="60%"><br><br>
* **EPIC 1 - BASE SETUP**<br>
    -1A Create<br>
    <img src="static/images/epic-1.png" width="60%"><br><br>
</details><br><br>

## Features

### Existing Features and sub-pages<hr>

#### Feature 1


### Potential Future Features

## Responsive Layout and Design
How the breakpoints are set.

**Tested devices:**

    - iPhone 13
    - MacBook Pro 


## Tools Used

[GitHub](https://github.com/) - used for hosting the source code of the program<br>
[Visual Studio](https://code.visualstudio.com/) - for writing and testing the code<br>
[Heroku](https://dashboard.heroku.com/) - used for deploying the project<br>
[ElephantSQL](https://www.elephantsql.com/) - For PostgreSQL database<br>
[Balsamiq](https://balsamiq.com/wireframes/) - for creating the wireframes<br>
[LucidChart](https://www.lucidchart.com/) - used for creating the Flowchart and Database relational schema<br>
[Favicon.io](https://favicon.io/) - used for generating the website favicon<br>
[TinyPNG](https://tinypng.com/) - for compressing the images<br>
[Grammarly](https://app.grammarly.com/) - for correcting text content<br>
[Font Awesome](https://fontawesome.com/) - for creating atractive UX with icons<br>
[Bootstrap5](https://getbootstrap.com/) - for adding predifined styled elements and creating responsiveness<br>
[Google Fonts](https://fonts.google.com/) - for typography<br>
[Code Institute Pylint](https://pep8ci.herokuapp.com/) - used for validating the python code<br>
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - used for validating the HTML<br>
[CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - used for validating the CSS<br>
[Firefox dev tools](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/open_the_inspector/index.html) - for debugging the project<br>
[Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - for debugging the project<br>
[W.A.V.E.](https://wave.webaim.org/) - for testing accessibility<br>
[Cloudinary](https://cloudinary.com/) - for storing static data<br>
Chrome LightHouse extension - for testing performance<br>

### Python packages

* Django (Framework)
* django-allauth (Library)
* django-bootstrap-datepicker-plus (Library)
* django-crispy-forms (Library)
* cloudinary (Library)
* gunicorn (Web Server)
* psycopg2 (Library)


## Testing
The testing documentation can be found at [TESTING.md](TESTING.md)

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

### Media

### Code

* Further studies with [Net Ninja](https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc)
* Help with Bootstrap from their own excellent [documentation](https://getbootstrap.com)
* Database setup and much more with [Codemy.com](https://www.youtube.com/watch?v=A1nqCgAM6CE)
* Automated testing with [CodingEntrepeneurs](https://www.youtube.com/watch?v=5E_xLmQXOZg)
* Code from Gareth McGirr's [project](https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak) used and customized for table verification
* A lot of time has been spent on re-watching Code Institutes splendid videos on Agile Methodologies, Django and Python to find solutions to problems.

## Acknowledgements









To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---




Make sure to remove the DISABLE_COLLECTSTATIC config var from heroku before final deployment.