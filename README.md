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
- [Libraries Used](#libraries-used)
- [Programs Used](#programs-used)

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
    - ## Visual Design

    ### Typography

    ### Color Scheme

  # Agile Methodology

# Features

   ## Existing Features

   - ### CRUD

   - ### Other Features

   - ### Future Features

   ## Technology

   - ### Languages Used

   - ### Libraries Used

   - ### Programs Used

   ## Testing

   - ### Automated Testing

   - ### Manual Test Cases

   - ### Code Validation

   - ### Lighthouse

   - ### Debugging

   - ### Test on Different Browsers and Screen Sizes

# Deployment

# Credits

   ## Resources Used

   ## Content 

   ## Honourable mentions


   [Back to Top](#contents)## Credits