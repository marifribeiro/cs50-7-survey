#CS50's Survey

##Introduction

This application was one of the 7th week's exercises of Harvard's CS50 - Introduction to Computer Science online course.
You can learn more about CS50 at [Harvard's CS50](https://online-learning.harvard.edu/course/cs50-introduction-computer-science).

The exercise proposes that we:
* Implemented a web application that enables the user to fill out a form, which the fields are up to the student's choice, as long as the form is "a la Google Forms" 
* The results are saved in a CSV file on the server
* The results are showed in a table a la Google Sheets


##How was this made
This application uses Python 3, HTML and styling with Bootstrap.

##Access it
My application is available at [cs50-7-survey.herokuapp](http://cs50-7-survey.herokuapp.com/form).

##Run on your own
You will need [Python](https://www.python.org/downloads/) and [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/) installed on your computer to run this application.

Start by installing [Python 2.7.9](https://www.python.org/downloads/release/python-2717/) or above.
Once you have Python, run the following commands:

To install this project's dependecies, run:

`pip3 install -r requirements.txt`

Install Flask:

`sudo apt install python3-flask`

Define the correct file as the default Flask application:

Unix Bash (Linux, Mac, etc.):

`export FLASK_APP=hello`

Windows CMD:

`set FLASK_APP=hello`

Windows PowerShell:

`$env:FLASK_APP = "hello"`

Run Flask and you're good to go!

`flask run`