# WeConnect

WeConnect provides a platform that brings businesses and individuals together. This platform creates awareness for businesses and gives the users the ability to write reviews about the businesses they have interacted with. 

# Features

User are able to perform the following functions;

* Register a business 
* Update a business profile
* Remove business
* Post a review for a business
* Get all the reviews for a business
* Search for businesses
* Filter businesses by location	
* Filter businesses by category

# Prerequisites

The templates make use of HTML and Css and will accomadate future integration of a python SQLAlchemy database. This program can run on any web browser conviniently

# Built With

* Html
* Css
* Python Flask 
* SQLAlchemy

# Api Installation

To set up WeConnect API, make sure that you have python3, postman and pip installed.
Use virtualenv for import modules management.

| EndPoint	| Functionality|
|-----------| -------------|
POST /api/auth/register | Creates a user account
POST /api/auth/login | Logs in a user
POST /api/auth/logout	| Logs out a user
POST /api/auth/reset-password	| Password reset
POST /api/businesses	| Register a business
PUT /api/businesses/<businessId> | Updates a business profile
DELETE /api//businesses/<businessId> | Remove a business
GET  /api/businesses | Retrieves all businesses
GET  /api/businesses/<businessId>| Get a business 
POST  /api/businesses/<businessId>/reviews | Add a review for a business
GET  /api/businesses/<businessId>/reviews | Get all reviews for a business



# Contributing

1. Fork this project to your GitHub account.
2. Create a branch for version control.
3. Proceed to make modifications to your fork.
4. Send pull request from your fork's branch to my master branch.

# Guidelines | How to run the app and tests

- Install flask and create a virtual environment. 
- Run flask run to execute the server 
- To test the application, install nosetests and run from the root directory.

# Author 

* Kevin Bett

# Acknowledgments

* Andeka Kenya
* Cohort25
* Game-of-codes

# User interface

![screenshot](https://github.com/kevinbett/WeConnect/blob/feature/designs/UI/img/login.PNG)

# License

@AndelaKenya
