# Vanhackathon
First of all, thank You for this opportunity!

# Frontend application:
Let's start with NodeJS. It's really easy to install & now includes NPM. You should be able to run the following command after the installation procedure below.

$ node --version
v10.5.0

$ npm --version
6.1.0

# Node installation on OS X
You will need to use a Terminal. On OS X, you can find the default terminal in /Applications/Utilities/Terminal.app.

Please install Homebrew if it's not already done with the following command.
$ ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

If everything when fine, you should run
$ brew install node

# Install application
$ git clone https://github.com/alexrosa/7shifts
$ cd 7shifts/frontend
$ npm install

# Start & watch
$ npm start

# Simple build for production
$ npm run build

# Backend application:
The backend solution was developed using Python 3 and Flask and I picked it because Python and Flask is very light and fit very well with this task.

# Installing Python on OSX:
Please, first of all, check if Python is installed in your system:

$ which python

or

$ which python3

If this command returns /usr/bin/python it means that Python is already installed in your system.

# Installing Python
Please, to install Python follow this link: http://programwithus.com/learn-to-code/install-python3-mac/

# Installing pip
$ sudo easy_install pip

Now please, install the third-party

$ pip install -r requirements.txt

# Running the application
Open your command line

$ python api.py

# TODO LIST:

1 - Processing data -> calculate hours;

2 - Storage of the processed data in a database;

