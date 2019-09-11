# PPA1---Intro to Unit-Testing T/BDD
## CIS4930 - Software Testing for Continuous Delivery Assignment

### Naming and Organizational Conventions
Unit tests are going to be named after the function that they are testing. Usually they will be named in the following format hhhh_Unit_Test.py, where hhhh is the name of the file/function that they are testing. Each of the unit tests has three funtions one called the *output_test()*, another called the *input_test()*, and lastly one called *stats()*. None of these functions take in any inputs. The output_test() tests the functionality by giving the function being tested some valid inputs and checking if the function returns a correct value. The input_test() on the other hand gives the function invalid inputs and checks whether the function returned an error message or not. The stats() function simply shows the number of passed and failed tests, and the percentage of passed tests.
You can run all the tests by running the Unit_Tests.py file which just calls all of the functions in all of the unit tests for you.

### Setup and Execution Instructions
For this assignment I used the **Python 3.6.8** programming language, the **Ubuntu 18.04.3 LTS** operating system, and the **Coverage.py, version 4.5.4 with C extension** tool. Download Links Below.

Instructions to run the programs:
1. Get the Ubuntu 18.04.3 LTS.
2. Install Python 3.6.8. Ubuntu should come wiht Python installed, however if it doesn't you can either use the link below or open the terminal and use the commands:
$ sudo apt-get update
$ sudo apt-get install python3.6
3. Get Coverage.py if you wish to test for code coverage. To get it use the link below and follow the instructions given (Make sure to download this to the same directory that the tests are on).
4. Download the program and the unit tests, leave them in the same directory.
5. At this point you can either run* PPA1.py in order to access the menu and use the program normally or run Unit_Tests.py to run the unit tests

* In order to run the program go to its directory in the terminal and type python3 *programname*

Intructions to run Coverage.py:
1. Go to the directory that contains the program files
2. Type coverage run *program name*
3. After the execution has completed, type coverage report -m to view a the code voverage report

Download Links:
Python 3.6.8 - https://www.python.org/downloads/release/python-368/
Ubuntu 18.04.3 - https://ubuntu.com/download/desktop
Coverage.py - https://coverage.readthedocs.io/en/coverage-4.2/install.html

### Report Output
![Unit Test Output part 1](/PPA1 Images/Unit_Test_Output1.png)
![Unit Test Output part 2](/PPA1 Images/Unit_Test_Output2.png)
### Test Coverage Report

### Student Overview
Before beggining this assignment I had very little unit testing & TDD experience. Currently, I think that unit testing & TDD are very useful and can help developers better the quality of their code, however it is also very time consuming making it less desirable in small and simple projects. I think that unit testing & TDD can be very useful in real projects that involve complex algorithms and multiple people working on the same feature as it makes it easier for both novice and experienced developers to produce functional and reliable code. The benefits of TDD is that it gives developers confidence in pushing out new features and changing old ones; the drawbacks is that it substantially increases the development time in the short term. - *Danilo De Souza*
