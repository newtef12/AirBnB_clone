#  AirBnB clone - The console

## Project Description

This is the first part of the AirBnB clone project where we worked on the backend of the project whiles interfacing it with a console application with the help of the cmd module in python.

Data (python objects) generated are stored in a json file and can be accessed with the help of the json module in python

## Description of the command interpreter

The interface of the application is just like the Bash shell except that this has a limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website.

This command line interpreter serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

## Available commands and what they do

| Command    |              Description                                                                                             |
|:----------:|:-------------------------------------------------------------------------------------------------------------------- |
| EOF or     |  Exit the program                                                                                                    |
  quit
| Usage      |  By itself                                                                                                           |
| Help       |  Provides a  text describing how to use a command                                                                    |     | create     |  Creates a new instance of a valid Class, saves it (to the JSON file) and prints the id.                                                   Valid classes are: BaseModel, User, State, City, Amenity, Place, Review.                                                               |                                                                                                                      |

## Format of Command

In order to give commands to the console, these will need to be piped through an echo in case of Non-interactive mode.

In Interactive Mode the commands will need to be written with a keyboard when the prompt appears and will be recognized when an enter key is pressed (new line). As soon as this happens, the console will attempt to execute the command through several means or will show an error message if the command didn't run successfully. In this mode, the console can be exited using the CTRL + D combination, CTRL + C, or the command quit or EOF.

## Testing

Unittests for the AirBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:

$ python3 unittest -m discover tests
Alternatively, you can specify a single test file to run at a time:

$ python3 unittest -m tests/test_console.py

## Authors

Joseph_IZ Akharume || ijeborjoe@gmail.com
