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
![search](https://i.imgur.com/cxrzWQI.jpg)

## Process
When breaking down this project, I decided to do so in what seemed like the most logical order. First I tackled the database/API, then I moved onto the backend, where I built my User model and other respective methods, structured my seeds file and got started on my .js files. Once this structure was in place, and I had something to work with.
![filepaths](https://i.imgur.com/2NWljjj.png)

A challenge for me initially was getting my edit function to work properly. The reason why this proved to be so challenging was primarily because of the data that was being sent to the frontend from my backend. In order the edit a book, I need to be able to get the book by ID but the information that was being posted was incorrect because not all fields were being acquired, specifically my authors. In order to fix this problem, I had to create a dropdown and populate it with all the authors in my seeds.
![dropdown](https://i.imgur.com/6Ltw53G.jpg)

When it came to the homepage, I had a couple of different approaches. Initially I thought it would be better to have a static image on the page, with some information describing my website to users with a CTA (Call to action) that would prompt the user to sign up. In the end I settled for keeping the CTA as it was but instead of having a static background image, I decided to have the images on the homepage transition to different images on a set interval of 4 seconds.

To achieve this, I had to create a separate file path of images in an array that will be displayed on the homepage background. Then import those images into the home file path and then set them on an interval of 4 seconds on an ease transition method in scss. To make the visual transition look seamless.
![homepage](https://i.imgur.com/62CSZFi.jpg)


## Challenges
- Managing expectations: This was essential when it came time to decide on which features to keep and which ones to abandon because of the time available. More often than not I wanted to make sure that I could get as many features as I wanted, in, as possible. Though, that was not always something I could do and as a result I found it quite challenging. 

- Getting the user ranking system in place

- Time Constraints: I had one week to work on this project, and so I was not able to do all the things I wanted to do. This was always to be expected when starting the project, nevertheless it was still a challenge at times, to decide on which things I should allocate the most time and attention. 


## Wins
- Reaching C.R.U.D (Create Read Update Delete)
- Attention grabbing homepage (Image transition feature)
- Fully functional search feature (Enabling the ability to search through the archives using RegEx)
- Loading page
- Infopage
- Register
- Login
- Edit
- Delete



## Future Features
Initially I wanted more features in my project but with only a weak, there was only so much I could do. 
Some features I will add in the future: 
- Fully functional review and commenting system
- Ranking System for users
- Upvote feature
- Save book feature

## Timeframe
7 days

## Tech used
HTML5, XML
SCSS, CSS, Bulma
JavaScript (ES6): React, Node.js - Express
Python
Yarn
