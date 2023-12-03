# Secret Agent Assist
- Updated to version 2.0 

## Project Description
A quick and easy place for our secret agents to find out some information about their next mission and objectives! 

## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [Logic](#logic)
- [Testing](#testing)
- [Bugs](#bugs)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)
- [Deployment](#deployment)


## Installation
### Environment
- You need to install [Python](https://www.python.org/downloads/) and [NodeJS](https://nodejs.org/en/download).  
- Clone from GIT repo `git clone https://github.com/ivankrauseza/ci-project3.git`.

### Installed Python modules
- Install DateTime:  `pip install datetime` 
- Install GeoIP:  `pip install python-geoip` 
- Install Colorama:  `pip install colorama` 


## Features
### Get current date and time
This is to personalise the greeting (morning, afternoon, evening)  
![Greeting](/images/greeting.png)  

### Color coding
Add colorama for color coding some of the print() statements.  
| GREEN | YELLOW | CYAN | RED |

### GeoLocation
Fetches GPS Co-ordinates of the next target.  
![Location](/images/location.png)  

## Logic
### Basic Flowchart  
![Flowchart](/images/Flowcharts.png)  
- The user starts a session by inputting a valid Agent Code '007' or '47' as any other input will fail.  
![step 1](/images/step1.png)  
- The user must then choose 1 of 4 options to proceed to the information related to each option.
- Option 1 :: Explains the next mission.  
![step 2](/images/step2.png)  
- Option 2 :: Explains how to get travel information and equipment.  
![step 3](/images/step3.png)  
- Option 3 :: Accept or Reject the mission.
- Option 4 :: Terminate the session.  
![step 5](/images/step5.png)  
- The user can return to the main menu or end the session after each option.


## Testing

### Manual Testing
| Test Function | Action    | Result    |
| ---           | ---       | ---       |
| agent_code()  | In order to access the application, the user has to enter a specific agent code from a list of predefined options found in the 'code_options' variable. The application denies access to the user if the code is invalid. If the code is inavalid, send a response back to the user for a possible reason why they cannot access the application. | PASS: The function works as expected |
| greeting      | When the agent successfully enters the application, the app detects current time and displays a message of either 'good morning', 'good afternoon' or 'good evening' to the user as well as the exact time they started their session as defined in the 'current_time' and 'greeting' variables  | PASS: The function works as expected |
| show_options() | Below the greeting message, the user is presented with a numbered list of options. They will input a number from 1-4 and press the 'enter' key which will call the option_responses() function. The user can only input numbers '1', '2', '3' in order to view the next mission details and accept/reject the mission and the user can exit the application if they insert '4'.  | PASS: All numbers 1-4 respond as expected. |
| 1 : option_responses() > answer_one() | When the user chooses option 1, the answer_one() function is called detailing the mission target details. This information includes the use of the Geopy package to display the address and gps co-ordinates of the the next target. | PASS: both option_responses() and answer_one() function as expected. |
| 2 : option_responses() > answer_two() | When the user chooses option 2, the answer_two() function is called detailing the instructions to collect equipment and documents for the next mission. | PASS: both option_responses() and answer_two() function as expected. |
| 3 : option_responses() > answer_three() | When the user chooses option 3, the answer_three() function is called asking the user if they accept the mission or not by entering 'y' for yes or 'n' for no in either upper or lowercase. If they choose yes, the app responds to the user confirming the mission is accepted and they are logged out of the application. If they choose not to accept the mission, the app responds with a message confirming the user did not accept the mission and then the application terminates the session. | PASS: both option_responses() and answer_three() function as expected. |
| continue_session() | After responses '1' and '2', the user is asked if they would like to continue the session or not by entering 'y' for yes or 'n' for no in either upper or lowercase. If yes the show_options() function is called and the user can choose from the options 1-4 again. If the user chooses no, the the application terminates. | PASS: functions as expected. |
| 4 : quit() | if the user chooses option 4 from the main menu, the application will run the default quit() function and terminate the session. | PASS: functions as expected. |
||||


### PEP8
Manual testing performed in https://www.pythonchecker.com/ and https://pep8ci.herokuapp.com/ which yielded no errors.

![PEP8 PythonCehcker](/images/PEP8_Test.png)  

![CI Python Linter](/images/ci_python_linter.png)  

Main errors related to 'length of line too long' and also fixed spacing, line breaks and comment position.  

In the PEP8 Validator, it suggested putting a space around '=' in 'colorama.init(autoreset=True)' but the python linter in VSCode highlights the space as an error and recommends remove the spaces. After reading further on https://pypi.org/project/colorama/ I have updated the import as follows:  
Before:
```
import colorama
from colorama import Fore
colorama.init(autoreset=True)
```
After:
```
from colorama import Fore, init
init()
```

PEP8 Validator suggests adding whitespace around the operators with 'current_time = datetime.now().strftime("%H:%M:%S")' however this is not required:
```
current_time = datetime.now().strftime("%H:%M:%S")
```

## Bugs
### Version 1
- B1 :: Repeat 'Would you like to continue' after selecting 'Y', should only display options with input form.
- B2 :: Entering any letter when choosing from the main options menu [1-4] loads an integer error.
### Version 2
- B3 :: Initial errors on first load

## Resolved Bugs
### Version 1
- B1 :: Seems to be resolved by moving the global call for the function to within the function itself.
- B2 :: Fixed by using Try/Except from [source](https://www.includehelp.com/python/asking-the-user-for-integer-input-in-python-limit-the-user-to-input-only-integer-value.aspx)
### Version 2
- B3 :: changed 'import datetime' to 'from datetime import datetime' and restructure greeting variable.


## Authors
<bold>Ivan Krause</bold>

## Acknowledgments
- README Structure (ChatGPT)
- [Python Functions](https://www.w3schools.com/python/python_functions.asp)
- [Python Date and Time](https://www.geeksforgeeks.org/get-current-date-and-time-using-python/)
- [Python options selector](https://bobbyhadz.com/blog/python-select-option-input)
- [Get Location](https://pythonhosted.org/python-geoip/)
- [Colorama Tutorial](https://www.youtube.com/watch?v=u51Zjlnui4Y)

## Deployment
- Version Control via GitHub

### Deployed to Heroku
- App Name - ivankrause-ci-project3
- Region - Europe
- Settings - Add buildpack - Python & NodeJS
- Deployment Method - Connect to Github
- Choose Repository - ci-project3
- Branch - main
- Automatic Deploys - Enable Automatic Deploys
- Manual Deploys - Deploy Branch 
- APP - https://ivankrause-ci-project3-36718a380df7.herokuapp.com/