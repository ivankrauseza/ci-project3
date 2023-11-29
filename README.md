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
- Install PyTest:  `pip install pytest` 


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
### PEP8
Testing performed with https://www.pythonchecker.com/  

In the PEP8 Validator, it suggests putting a space around '=' in 'colorama.init(autoreset=True)' but the python linter in VSCode highlights the space as an error and recommends remove the spaces. After reading further on https://pypi.org/project/colorama/ I have updated the import as follows:  
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

## PyTest
'PyTest'  
![PYTEST](/images/pytest.png)  

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