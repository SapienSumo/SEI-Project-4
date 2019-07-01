# General Assembly SEI-Project-4: Online Library (Apochrypha)

## Timeframe
7 days

## Tech used
HTML5, XML
SCSS, CSS, Bulma
JavaScript (ES6): React, Node.js - Express
Python
Yarn
Git + GitHub

## Installation
Clone or download the repo
In terminal run 2 things: yarn run:server, yarn run:client

## My Web Application - Apochrypha
link to hosted version ----> (apochrypha.herokuapp.com)


## Application Overview
The premise of my Web App, wasn’t to try and create something that had never been done before, but instead to demonstrate what I had learned so far on the course, whilst challenging myself to create something unique that I hadn’t previously done on the course.
![homepage](https://i.imgur.com/RwArpUS.jpg)


## Process
When breaking down this project, I decided to do so in what seemed like the most logical order. First I tackled the database/API, then I moved onto the backend, where I built my User model and other respective methods, structured my seeds file and got started on my .js files. Once this structure was in place, and I had something to work with.


A challenge for me initially was getting my edit function to work properly. The reason why this proved to be so challenging was primarily because of the data that was being sent to the frontend from my backend. In order the edit a book, I need to be able to get the book by ID but the information that was being posted was incorrect because not all fields were being acquired, specifically my authors. In order to fix this problem, I had to create a dropdown and populate it with all the authors in my seeds.


When it came to the homepage, I had a couple of different approaches. Initially I thought it would be better to have a static image on the page, with some information describing my website to users with a CTA (Call to action) that would prompt the user to sign up. In the end I settled for keeping the CTA as it was but instead of having a static background image, I decided to have the images on the homepage transition to different images on a set interval of 4 seconds.

To achieve this, I had to create a separate file path of images in an array that would be displayed on the homepage background. Then import those images into the home file path and then set them on an interval of 4 seconds on an ease transition method in scss. To make the visual transition look seamless.



## Challenges
- Managing expectations
- Getting forms to look how I wanted them to
- Time Constraints


## Wins
- Reaching C.R.U.D
- Attention grabbing homepage
- Fuully functoinal search feature
- User friendly features: loading page, infopage - register to login, to user profile, to - edit profile or matches etc.
- I had fun making it


## Future Features
Initially I wanted far more in my project but with only a weak, there was only so much I could do. 
-Fully functional review and comment features
-Ranking System for users
-Upvote feature# General Assembly SEI-Project-4: Online Library (Apochrypha)

## Timeframe
7 days

## Tech used
HTML5, XML
SCSS, CSS, Bulma
JavaScript (ES6): React, Node.js - Express
Python
Yarn
