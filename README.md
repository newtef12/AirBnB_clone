Project Overview
This project marks the initial phase of developing an AirBnB clone, focusing on the backend while integrating it with a console application utilizing Python's cmd module.

Data Management
The generated Python objects are stored in a JSON file, which can be accessed and manipulated using Python's json module.

Command Interpreter Overview
The application interface functions similarly to the Bash shell but supports a limited set of commands specifically designed for the AirBnB website. This command line interpreter acts as the frontend, allowing users to interact with the backend built using Python's object-oriented programming.

Available Commands and Their Functions
Command	Description
EOF or quit	Exit the program
help	Provides usage instructions for commands
Command Usage Formats
Non-Interactive Mode: Commands need to be piped through an echo.
Interactive Mode: Users type commands directly at the prompt. Commands are executed upon pressing the enter key. The console can be exited using CTRL + D, CTRL + C, quit, or EOF.
Testing
Unittests are located in the tests folder. To run all tests, use:

ruby
Copy code
$ python3 -m unittest discover tests
To run a specific test file, use:

shell
Copy code
$ python3 -m unittest tests/test_console.py
Authors
Joseph_IZ Akharume | ijeborjoe@gmail.com
