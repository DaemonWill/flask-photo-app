# flask-photo-app
A simple flask application that allows users to upload photos and have the image shown to them

[![Build Status](https://travis-ci.org/DaemonWill/flask-photo-app.svg?branch=master)](https://travis-ci.org/DaemonWill/flask-photo-app)

==================================================================
### App-Link : https://rocky-shore-70939.herokuapp.com/

### Author : Daimen Q. Williams
###### [DaimenWill@gmail.com](mailto:DaimenWill@gmail.com)

---
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Overview:
  * Technologies Used
  * Environment Setup
  * Using the Application
  * Testing

-------


# Technologies Used

#### This webapp runs on the Flask Framework. All you'll need is Python 3+ and install the dependencies listed in the requirements.txt through pip. An explanation of the steps needed to setup the project is in the "Environment Setup" portion.

Technologies needed for local setup:
  1. Python 3.6.1
  4. Libraries for flask and other integration dependencies (check _requirements.txt_, setup explained below)

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-------

# Environment Setup

Once Python 3.6.1 is installed -

  1. In the project's root folder, call a _"python -m venv flask"_ to have a virtual env setup with the libraries we'll include
  2. Install the libraries in the requirements.txt through the command `flask\Scripts\pip install -r requirements.txt` (That's if you're on a windows OS, if you're on mac/linux, try `flask/bin/pip install -r requirements.txt`)
  3. If the above doesn't work out, try to install the following dependencies in the virtual environment one at a time (not all are needed but if you want a local heroku instance up and running it's best to import these all):
    * click==6.7
    * Flask==0.12.2
    * gunicorn==19.7.1
    * itsdangerous==0.24
    * Jinja2==2.10
    * MarkupSafe==1.0
    * Werkzeug==0.14.1
    * flask-wtf
    * flask-babel
    * coverage

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-------

# Using the Application

There is a sample of the application currently hosted on heroku at: https://rocky-shore-70939.herokuapp.com/

You can run the app locally in the root folder through the command:

`flask\Scripts\python run.py` for windows
`flask/bin/python run.py` for linux/osx

The application is fairly simple; using Flask for the server logic, the front accepts all image files submitted and shows the user the picture once it's accepted. 


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-------

# Testing
There are a few test cases using the Werkzeug libraries and python's unittest. The file is in the root folder as test.py, run the following command to run the tests:

`flask\Scripts\python test.py` for windows
`flask/bin/python test.py` for linux/osx
