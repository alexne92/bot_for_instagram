# Instagram bot for follow and likes

## About

bot_for_instagram is a pure-python code to automate the process of several tasks in instagram.\
The purpose of this project is to help the user to perform the following operations:

- follow other users 
- like photos
- comment posts

All these operations are based on the hashtags that the user is interested into.

## Table of Contents:

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Quick Start](#quick-start)

## Requirements

- `Python 3`
- (During the initial creation of the project) `pip 19.2.3`

## Installation

The best way to install the requirements without having problems with the rest of python libraries that the user has already installed is to use a virtual environment.\
To create a new virtual environment use the following commands.

````bash
$ python3 -m pip install virtualenv
$ python3 -m virtualenv bot_for_instagram_env
````

The way to activate the new environment is the following:

````bash
$ source bot_for_instagram_env/bin/activate
````

To deactivate the virtual environment, just type:

````bash
$ deactivate
````

For the next step, the user has to install the proper requirements, which can be found in the requirements.txt file.\
To install the requirements directly from the file, use the following command:

````bash
$ pip install -r requirements.txt
````

## Configuration

Before using the bot, or whenever a change on the credentials is needed, the user has to use the create_credentials.py file.\
To do so, the user has to execute the following command:

````bash
$ python create_credentials.py -u <username> -p <password>
````

## Quick Start

Finally, to set the bot running, the user has to import the hashtags tha he/she is interested into as arguments.
The hashtags can be imported with the following command:

````bash
$ python insta.py <hashtag_1> <hashtag_2> ...
````

Note that the user is requested to add at least one hashtag!