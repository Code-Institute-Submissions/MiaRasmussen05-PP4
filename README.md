# Portfolio Project Website

This website was created for my 4th Portfolio Project with Code Institute. I decided to create a website to promote my skills and what I do. By both having a gallery, shop, portfolio, and a blog I can use all the things I love and promote myself as well. I used the idea of a shop to reach a bussines point of view, because more and more people shop online so they can get everything from everywhere. With a blog that takes a more of a social network point of view so conversation can be made and discussions can get started. A gallery to see the beauty in the world througt someone elses eyes.

[My Portfolio Project website on Heroku](https://portfolio-project4.herokuapp.com/)

![GitHub shield last commit](https://img.shields.io/github/last-commit/MiaRasmussen05/pp4?color=red)
![GitHub shield language count](https://img.shields.io/github/languages/count/MiaRasmussen05/pp4?color=orange)
![GitHub shield contributors](https://img.shields.io/github/contributors/MiaRasmussen05/pp4?color=yellow)
![GitHub shield top language](https://img.shields.io/github/languages/top/MiaRasmussen05/pp4?color=brightgree&label=html)

# Contents

[UX Design](#ux-design)
- [Strategy](#strategy)
  - [User Stories](#user-stories)
- [Scope](#scope)
- [Structure](#structure)
- [Skeleton](#skeleton)
  - [Wireframes](#wireframes)
- [Surface](#surface)
  - [Visual Design](#visual-design)
    - [Typography](#typography)
    - [Color Scheme](#color-scheme)

[Agile Methodology](#agile-methodology)

[Features](#features)
- [Existing Features](#existing-features)
- [CRUD](#crud)
- [Other Features](#other-features)
- [Future Features](#future-features)

[Technology](#technology)
- [Languages Used](#languages-used)
- [Libraries and Programs Used](#libraries-and-programs-used)

[Testing](#testing)
- [Automated Testing](#automated-testing)
- [Manual Test Cases](#manual-test-cases)
- [Code Validation](#code-validation)
- [Lighthouse](#lighthouse)
- [Debugging](#debugging)
- [Test on Different Browsers and Screen Sizes](#test-on-different-browsers-and-screen-sizes)

[Deployment](#deployment)

[Credits](#credits)
- [Resources Used](#resources-used)
- [Content](#content)
- [Honourable mentions](#honourable-mentions)

# UX Design
    
  ## Strategy
  
  ### __Typical Users__
  
  A typical Site User would be anyone who wants to see what the Admin can do. It would be users that want to hire, buy, or offer them a job while keeping up to date with what the admin is doing. And contact them with any inquiries

  The Site Admin will be the person that owns the page. It will be the person that creates all the content for the page so the users can comment, review, buy, and look at the content made.

- ## User Stories
  
  ### Site User
  - __Account Register:__ I can signup or login into an account, so I can access all items not available to unregistered users.

  - __Edit Profile:__ I can edit my personal profile to have my own user image, and decide what information gets put in.

  - __View Shop:__ I can view the shop items and see their detailed pages and add items to my cart when login in.

  - __Add Review:__ I can add a review to a shop item so that I can be a part of the rating and keep items up to quality.

  - __View Review:__ I can read individual reviews on the shop item so that I can make a qualified decision about the item.

  - __Edit Review:__ I can edit my own review so that I can change it again, or update it later.

  - __Add Comment:__ I can add a comment to a blog post so that I can be a part of the conversation.

  - __View Comments:__ I can read individual comments on a blog post so that I can read the conversation. 

  - __Edit Comment:__ I can edit my own comment so that I can change it again, or update it later.

  - __Like / Unlike:__ I can like or unlike a blog post so that I can interact with the content in the blog.

  - __Bookmark:__ I can bookmark or remove bookmarks again on blog posts to add to my favorites page on my profile so that I can decide which to save especially for removal again.

  - __View Portfolio Page:__ I can view the projects in the portfolio so that I can decide to click on a link to watch it more closely.

  - __View Gallery:__ I can view the images in the gallery so that I can click on an image to learn more about it and just look through images.

  - __View Profiles:__ I can view other people's profiles so that I can see who posted on blog posts and added reviews in the shop.

  - __Manage Cart:__ I can add, read, update, and delete items from my cart so that I can decide what I order directly in the cart.

  - __Order History:__ As a Site User I can read, update, and delete my orders until they get sent so that if I change my mind then I can update or delete my orders.

  - __All Orders:__ I can view all orders made by site users so that I can keep up to date with what has been ordered or removed.

  ### Site Admin
  - __Manage Blog Posts:__ I can create, read, update, and delete blog posts so that I can manage my blog content at all times.

  - __Manage Shop Items:__ I can create, read, update, and delete shop items so that I can manage my shop items at all times.

  - __Delete Review:__ I can delete all reviews to keep the content friendly and respectful, while users can only delete their own.

  - __Add Category:__ I can add categories to my shop and gallery if new categories are needed.

  - __Manage Portfolio:__ I can create, read, update, and delete projects for my portfolio so that I can easily manage what is shown and what is not.

  - __Manage Gallery:__ I can create, read, update, and, delete my images in the gallery so that new images are added often and information is kept up to date.

  - __Delete Comment:__ I can delete all comments to keep the content friendly and respectful, while users can only delete their own.

   ## Scope
  An MVP (Minimum Viable Product) approach was taken to the development of this site. The main features deemed as basic requirements for this site were:
  
  - Account Registration
  - CRUD Functionality (Both for Site User and Site Admin)
  - Device Responsiveness
  
  For a more detailed explanation of all existing features see [Existing Features](#existing-features). [Future Features](#future-features) were still within the possible scope of this project, they were not necessary at this point in time for the site to still work.

  ## Structure

  ### Site Navigation Flowchart

  Both Flow charts where made to see the structure of navigation on the page. The flowcharts were created with [Lucid](https://lucid.app/documents#/dashboard).

  ![Flowchart for admin](https://imgur.com/TVj2EKQ.png)

  ![Flowchart for users](https://imgur.com/wzskQyz.png)

  ## Skeleton

  ### Wireframes

  <details>
  <summary>Wireframes Home Page</summary>
  <a href="https://imgur.com/A6zbaaR"><img src="https://imgur.com/A6zbaaR.png" title="source: imgur.com" /></a>
  </details>
  <br>

  <details>
  <summary>Wireframes Shop Page</summary>
  <a href="https://imgur.com/YrbD5ys"><img src="https://imgur.com/YrbD5ys.png" title="source: imgur.com" /></a>
  </details>
  <br>

  <details>
  <summary>Wireframes Blog Page</summary>
  <a href="https://imgur.com/6FX8UKu"><img src="https://imgur.com/6FX8UKu.png" title="source: imgur.com" /></a>
  </details>
  <br>

  <details>
  <summary>Wireframes Portfolio Page</summary>
  <a href="https://imgur.com/iBGtkiu"><img src="https://imgur.com/iBGtkiu.png" title="source: imgur.com" /></a>
  </details>
  <br>

  <details>
  <summary>Wireframes Gallery Page</summary>
  <a href="https://imgur.com/JgzC7c8"><img src="https://imgur.com/JgzC7c8.png" title="source: imgur.com" /></a>
  </details>
  <br>

  <details>
  <summary>Wireframes Contact Page</summary>
  <a href="https://imgur.com/MUi2Uzf"><img src="https://imgur.com/MUi2Uzf.png" title="source: imgur.com" /></a>
  </details>
  <br>

  <details>
  <summary>Wireframes Login/Sign up</summary>
  <a href="https://imgur.com/2gJe4OR"><img src="https://imgur.com/2gJe4OR.png" title="source: imgur.com" /></a>
  </details>
  <br>

  ## Surface

    ### __Visual Design__

    ### Typography

    I went for the automatic font style to be my main font, but for the headings on my pages I went for a new font for the first letter to add a little style, the style chosen was 'Great Vibes' with a secondary font of 'cursive'.

    ### Color Scheme

    I went for a warm color scheme with brown colors with burgundy for the main color that is used to show buttons and some backgrounds to make all of these easily distinguishable between the browns.
    The color pallet was made with [Coolors](https://coolors.co/).

    ![Color Pallet](https://imgur.com/2MnPgXG.png)

  # Agile Methodology

  An Agile approach was taken for the management of this project.

  - User stories were written for each of the site's features.

  - The user stories were then managed in a Kanban board, which was created in GitHub Projects.

# Features

   ## Existing Features

- __Logo__

![Logo](https://imgur.com/23njbGW.png)

- __Navigation Bar__

Logged Out

![Logged out nav bar](https://imgur.com/U834sV5.png)

Logged In

![Color Pallet](https://imgur.com/LQzJN26.png)

- __The Home Page__

The home page is the first page a user sees, it shows a bit about the admin and about their services.

![Home Page](https://imgur.com/nQsGty5.png)

- __Footer__

![Footer big screens](https://imgur.com/lgUPnvU.png)

![Footer small screens](https://imgur.com/gDiibUG.png)

- __The Shop Page__

The shop page is where the user can look through the content and either click on the shop items page or just add it directly to the cart. The admin can on this page add a new shop item, edit or delete. 

![Shop Page](https://imgur.com/7WRYFBI.png)

- __The Blog Page__

The blog page is where the user can look through the blog post and find either a new one to read or click on it to read again. The admin can on this page click on the button to add a new blog post.

![Blog Page](https://imgur.com/vN7JZQE.png)



   - ### CRUD

   - __As a Visiting User:__
    - __READ__: A visiting user can view all the pages but can not interact with the cart, comments, or reviews.

  - __As a Site User:__
    
    __CREATE__: 
    - A site user can by login in create their own profile page. 
    - They can interact with the comments on a blog post.
    - Like blog posts and save them. 
    - Add reviews to the shop items.
    - Add shop items to their carts.

    - __READ__:
    - A site user can read everything on the pages.

    - __UPDATE__:
    - Site users can update their comments on a blog post.
    - They can update their reviews on shop items.
    - Update their carts.
    - Update their profiles.

    - __DELETE__:
    - Site users can delete their own comments on blog posts.
    - Delete their reviews on shop items.


  - __As Site Admin:__
    - __CREATE__:
    - The admin can create content on all pages: Shop, Blog, Gallery, and Portfolio.
  
    - __READ__:
    - The admin like the site user can read all content on the site.

    - __UPDATE__:
    - The admin can update content on all pages: Shop, Blog Post, Gallery, and Portfolio.

    - __DELETE__: 
    - The admin can delete content on all pages: Shop, Blog Post, Gallery, and Portfolio.
    - Admin can also delete comments and reviews from other users if they are against regulations. 

   - ### Other Features
   - Users are able to register and sign into the site through django-allauth
   
   ![Success message](https://imgur.com/SU8CvOH.png)

   - Success messages have been added to inform the User or admin when they have:
   - Signed in
   - Logged in
   - Logged out
   - Adds content to any page
   - Edites content on any page
   - Deletes content from any page
   - The user that contacts the admin gets an email send back to them.

   - ### Future Features

     - Site users can like shop items and images in gallery that then gets saved in favorites as well.

     - Site users can see each others profiles to see hat others have saved.

     - Site users can add stars for the photos in gallery give it a score.

     - Admin will be able to add a section only visible for logged in users on different pages with special content.

   ## Technology

   - ### Languages Used
     - HTML
     - CSS
     - JavaScript
     - Python
     - Django
     - Unitest (Django’s unit tests)

   - ### Libraries and Programs Used

     - Git - Was used for version control, the Gitpod terminal to commit and push to GitHub.

     - [GitHub](https://github.com/) - Was used to store the project code and display the project in GitHub Pages.

     - [Figma](https://www.figma.com/) - Was used to create the wireframes.

     - [Coolors](https://coolors.co/) - Was used for creating a pallet of the colors used.

     - [Lucid](https://lucid.app/) - Was used to create the flowcharts.

     - [Font Awesome](https://fontawesome.com/) - Was used to add icons for the social links in the footer.

     - Google Dev Tools- Were used to test and troubleshoot the webpage as well as fix problems with responsive design and styling.

     - [Google Fonts](https://fonts.google.com/) - Where used to import every font used in the website.

     - [Shields](https://shields.io/) - Was used to add different shields into the README. 

     - [Favicon](https://favicon.io/) - Was used to take the logo and make it into a favicon.

     - [Google Fonts](https://fonts.google.com/) - Where used to import every font used in the website.

     - [Heroku](heroku.com) - Where used for Deployment.

     - [Bootstrap](https://getbootstrap.com/) - Where used for CSS and some HTML.

     - [ElephantSQL](https://www.elephantsql.com/) - Where used for PostgreSQL database hosting.

     - [Cloudinary](https://console.cloudinary.com/) - Where used to save static media files.

   ## Testing

   - ### Automated Testing

   - ### Manual Test Cases

   - ### Code Validation

   - ### Lighthouse

   - ### Debugging

   - ### Test on Different Browsers and Screen Sizes

# Deployment

## Installing Django and Supporting Libraries:

- First __Install Django__ and __gunicorn__: pip3 install 'django<4' gunicorn
- __Install Django database__ and __pyscopg2__: pip3 install dj_database_url psycopg2
- Then __Install Cloudinary:__ pip3 install dj3-cloudinary-storage
- And then create the requirements.txt file by writing: pip3 freeze --local > requirements.txt

## Creating the Django Project and App:

- After installing the needed Libraries then 
 you create __the Django project:__ django-admin startproject <NAME> .
- Create the <NAME> app: python3 manage.py startapp <NAME>
- Then add the <NAME> app to __"INSTALLED_APPS"__ in the settings.py file

## Create the Heroku App:

- Log in on Heroku and then go to the Dashboard
- Click "__New__" and select then "__Create new app__" from the drop-down menu in Heroku
- Add a new unique app name (UNIQUE-NAME) and choose the relevant region
- Click the "__Create app__" button

## Creating (ElephantSQL) the PostgreSQL database:

- Log on to ElephantSQL
- Then click "__Create New Instance__"
- Set up a then plan by giving it a name and then select the "Tiny Turtle" for the free plan.
- Then click "__Select Region__" and choose the appropriate data centre which is the nearest by location
- Click "__Review__"
- Check over all details and then click "__Create Instance__"
- Back to the dashboard and click on the name of the newly created database
- Copy the database URL from the page from the details section

## Create env.py file:

- You need to create env.py file, and then checking it is included in the .gitignore file
- Add then "__import os__" to env.py file at the top
- Set the environment variables

- For DATABASE_URL to the URL copied from ElephantSQL: os.environ["DATABASE_URL"]="<copiedURL>"
- Set SECRET_KEY variable can be any multiple letters from 20 +: os.environ["SECRET_KEY"]="MY_SECRET_KEY"
- Add any others that is needed as well

## Modifying Settings:

- First connect the Django project to the env.py file by adding the following to the top of the settings.py file:

  import os
  import dj_database_url
  if os.path.isfile('env.py'):
      import env

- Then you replace the insecure secret key provided by Django in the settings.py file with: SECRET_KEY = os.environ.get("SECRET_KEY")="MY_SECRET_KEY"
- Connect to the new database by first commenting out the provided DATABASE variable in the file and then under it adding:

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

- Make sure to save the settings.py file after

## Connecting Cloudinary:

- Log on to Cloudinary
- From the Cloudinary dashboard, you copy the API Environment variable
- Add this to the env.py file: os.environ["CLOUDINARY_URL"] = "<COPIED_CARIABLE>"
- Then in the INSTALLED_APPS list of the settings.py file, above django.contrib.staticfiles you add: __'cloudinary_storage',__
- Then you add, below django.contrib.staticfiles: __'cloudinary',__
- Add to the settings.py, to make sure to define Cloudinary as the static file and media storage:

    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

## Add Heroku Config Vars:

- In Heroku dashboard you need to add a few things 
- Go to settings tab on Heroku
- Then add five new config vars:
    1. DATABASE_URL (value "<copiedURL>")
    2. SECRET_KEY (value "MY_SECRET_KEY")
    3. PORT (value "8000")
    4. DISABLE_COLLECTSTATIC (value "1") 
    - The last step will be removed again before deployment
    5. CLOUDINARY_URL (value "<COPIED_CARIABLE>")

## Allowing Heroku as the Host:

- Add under the BASE_DIR line of the settings.py file, replace the templates directory with: TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
- Then within the TEMPLATES array of settings.py file, you then replace the templates directory with: 'DIRS': [TEMPLATES_DIR],
- You then in the settings.py file, add your Heroku Hostname to the ALLOWED_HOSTS: ALLOWED_HOSTS = ['NAME_OF_HEROKU_APP.herokuapp.com', 'localhost']
- You then need to create three new folders in the top level directory: "__media__", "__static__" and "__templates__"
- Create the Procfile and only add: web: gunicorn PROJ_NAME.wsgi
- Save and commit
- Push the project to Github again
- Connect your github account to your Heroku through the Deploy tab on Heroku
- Connect your github project repository, and then click on the "Deploy" button that makes most sence to you "Auto" or "Manual"

# Credits

## Resources Used
- Code Institutes 'Hello Django Videos'
- Code Institutes 'I Think Therefore I Blog Videos'
- [Stack overflow](https://stackoverflow.com/questions/15845116/how-to-set-min-length-for-models-textfield) learning max_lenth in models.

- [Stack overflow](https://stackoverflow.com/questions/4101258/how-do-i-add-a-placeholder-on-a-charfield-in-django) to learn how to put a placholder on a CHarField in a form.

- [Learning about Electronics](http://www.learningaboutelectronics.com/Articles/How-to-add-a-price-field-to-a-database-table-in-Django.php) to learn how to add price in models.

- [dev](https://dev.to/greenteabiscuit/deleting-the-form-field-label-in-django-1i20) how to add the labels dictionary in the form.

- [Geeksforgeeks](https://www.geeksforgeeks.org/python-random-sample-function/) learning about using random sample function.

- [Youtube](https://www.youtube.com/watch?v=J7xaESAddDQ&t=67s) on how to update and edit a blog post.

- [Youtube](https://www.youtube.com/watch?v=H4QPHLmsZMU) on how to create a bookmark.

## Content 
- All images, logo, and text have been made and written by me.

## Honourable mentions
- [Thomas Faulkner/Tom F](https://github.com/TuckerFaulk/) for the big help with understanding the big work behind what needs to go in the README.


   [Back to Top](#contents)## Credits