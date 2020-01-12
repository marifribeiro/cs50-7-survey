# CS50's Survey

## Introduction

This application was one of the 7th week's exercises of Harvard's CS50 - Introduction to Computer Science online course.
You can learn more about CS50 at [Harvard's CS50](https://online-learning.harvard.edu/course/cs50-introduction-computer-science).

The exercise proposes that we:
* Implemented a web application that enables the user to fill out a form, which the fields are up to the student's choice, as long as the form is "a la Google Forms" 
* The results are saved in a CSV file on the server
* The results are showed in a table a la Google Sheets


## Created with
This application uses Python, HTML and styling with Bootstrap.

## Access
My application is available at [cs50-7-survey.herokuapp](http://cs50-7-survey.herokuapp.com/form).

## Run
You will need [Python](https://www.python.org/downloads/) and [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/) installed on your computer to run this application.

Start by installing [Python 3](https://www.python.org/downloads/). Here's a [guide on the installation](https://wiki.python.org/moin/BeginnersGuide/Download).
Once you have Python, and clonned this repository, run the following commands:

To install pip, run:

`sudo apt install python3-pip`

To install Flask, run:

`sudo apt install python3-flask`

To install this project's dependecies, run:

`pip3 install -r requirements.txt`

Define the correct file as the default Flask application:

Unix Bash (Linux, Mac, etc.):

`export FLASK_APP=application.py`

Windows CMD:

`set FLASK_APP=application.py`

Windows PowerShell:

`$env:FLASK_APP = "application.py"`

Run Flask and you're good to go!

`flask run`
