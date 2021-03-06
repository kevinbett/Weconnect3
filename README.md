[![Build Status](https://travis-ci.org/kevinbett/Weconnect3.svg?branch=ft-database-156041163)](https://travis-ci.org/kevinbett/Weconnect3)
[![Coverage Status](https://coveralls.io/repos/github/kevinbett/Weconnect3/badge.svg?branch=ft-database-156041163)](https://coveralls.io/github/kevinbett/Weconnect3?branch=ft-database-156041163)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f544ca7fd5424e969a3aa7503e1b1aa5)](https://www.codacy.com/app/kevinbett/Weconnect3?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kevinbett/Weconnect3&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/ed3bd87d71c43df42d64/maintainability)](https://codeclimate.com/github/kevinbett/Weconnect3/maintainability)

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

**EndPoint** | **Functionality**
--- | ---
POST `/api/v1/auth/register` | Creates a user account 
POST `/api/v1/auth/login` | Logs in a user
POST `/api/v1/auth/logout` | Logs out a user
POST `/api/v1/auth/reset-password` | Password reset
POST  `/api/v1/businesses` | Register a business
PUT `/api/v1/business/<businessId>` | Updates a business profile
DELETE `/api/v1/business/<businessId>` | Remove a business
GET  `/api/v1/businesses` | Retrieves all businesses
GET  `/api/v1/business/<businessId>` | Get a business 
POST  `/api/v1/business/<businessId>/reviews` | Add a review for a business
GET  `/api/v1/business/<businessId>/reviews` | Get all reviews for a business

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
