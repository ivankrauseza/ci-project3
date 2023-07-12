import datetime
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from geopy.geocoders import Nominatim


# Determine time based greeting message:
current_time = datetime.datetime.now().time()
morning_start = datetime.time(6, 0)
afternoon_start = datetime.time(12, 0)
evening_start = datetime.time(18, 0)
start_time = current_time.strftime("%H:%M:%S")

if morning_start <= current_time < afternoon_start:
    greeting = "\nGood morning"
elif afternoon_start <= current_time < evening_start:
    greeting = "\nGood afternoon"
else:
    greeting = "\nGood evening"


# Session Management
def continueSession():
    qbranch = ''
    while True:
        qbranch = input(Fore.YELLOW + "Would you like to continue? [Y/N]: ").lower()
        if qbranch == 'y':
            showQuestions()
            continue
        elif qbranch == 'n':
            print(Fore.RED + "\nSession terminated!\n")
            quit()
        else:
            print(Fore.CYAN + "\nPlease only enter Y for 'yes' or N for 'no'\n")
            continueSession()


# Answer 1
def ansA():
    print(Fore.CYAN + '\nTarget:')
    print(Fore.WHITE + 'Shinji Nakamora')
    print(Fore.CYAN + '\nObjective:')
    print(Fore.WHITE + 'Locate and extract target with minimal force. Required for urgent questioning!')
    print(Fore.CYAN + '\nCurrent Location:')

    # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")
    
    # entering the location name
    getLoc = loc.geocode("Paris, France\n")
    
    # printing address
    print(getLoc.address)
    
    # printing latitude and longitude
    print("Latitude = ", getLoc.latitude, "")
    print("Longitude = ", getLoc.longitude)
    print("\n")

# Answer 2
def ansB():
    print(Fore.WHITE + '\nYou parked your car at your local Supermarket\n')
    continueSession()

# Answer 3
def ansC():
    print(Fore.WHITE + '\nSomething from Q-Branch\n')
    continueSession()


# User Input
def answerQuestion():
    user_input = ''

    while True:
        user_input = int(input(Fore.YELLOW + '\nENTER NUMBER TO PROCEED:'))
        if user_input == 1:
            ansA()
            continueSession()
            continue
        elif user_input == 2:
            ansB()
            continue
        elif user_input == 3:
            ansC()
            continue
        elif user_input == 4:
            print(Fore.RED + "\nSession terminated!\n")
            quit()
        else:
            print('Type a number 1-4 please')
            continue

# All Options
def showQuestions():
    options = [Fore.WHITE + "1. NEXT TARGET", "2. TRAVEL ARRANGEMENTS", "3. ACCEPT MISSION", "4. TERMINATE SESSION"]
    for x in options:
        print(x+"")
    
    answerQuestion()

# Step 1: Ask for the user name:
def askName():
    name = input(Fore.YELLOW + "\nAGENT CODE:")
    if name == "007":
        print(Fore.GREEN + greeting+" "+name+", Your session is logged at: " +start_time+".\n")
        showQuestions()
    elif name == "47":
        print(Fore.GREEN + greeting+" "+name+", Your session is logged at: " +start_time+".\n")
        showQuestions()
    elif name == "":
        print(Fore.RED + "Your session cannot be started, please enter a valid Agent Code!")
        askName()
    else:
        print(Fore.RED + "Your session cannot be started due to an error!")
        askName()

askName()


