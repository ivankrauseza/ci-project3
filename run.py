import datetime
import colorama
from colorama import Fore
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
        qbranch = input(Fore.YELLOW + "Would you like to continue? [Y/N]:\n").lower()
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
    print(Fore.CYAN + '\nTravel Arrangements:')
    print(Fore.WHITE + 'Meet with Q at 11:11 tomorrow to pick up your Travel documentation and equipment:\n')
    print(Fore.CYAN + '\nCurrent Location:')

    # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")
    
    # entering the location name
    getLoc = loc.geocode("Dublin Zoo, Dublin, Ireland\n")
    
    # printing address
    print(getLoc.address)
    
    # printing latitude and longitude
    print("Latitude = ", getLoc.latitude, "")
    print("Longitude = ", getLoc.longitude)
    print(Fore.CYAN + '\nNotes:')
    print(Fore.WHITE + 'Q will be in a purple hoodie outside the Red Panda enclosure!:\n')
    print("\n")
    continueSession()


# Session Management
def ansC():
    acceptMission = ''
    while True:
        acceptMission = input(Fore.YELLOW + "DO YOU ACCEPT THE MISSION? [Y/N]:\n").lower()
        if acceptMission == 'y':
            showQuestions()
            continue
        elif acceptMission == 'n':
            print(Fore.RED + "\nSession terminated!\n")
            quit()
        else:
            print(Fore.CYAN + "\nPlease only enter Y for 'yes' or N for 'no'\n")
            ansC()


# User Input
def answerQuestion():
    user_input = ''

    while True:
        try:
            user_input = int(input(Fore.YELLOW + '\nENTER NUMBER TO PROCEED [1-4]:\n'))
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
        except ValueError:
                print('Type any number from 1-4 please')
                continue

# All Options
def showQuestions():
    options = [Fore.WHITE + "1. NEXT TARGET", "2. TRAVEL ARRANGEMENTS", "3. ACCEPT MISSION", "4. TERMINATE SESSION"]
    for x in options:
        print(x+"")
    
    answerQuestion()


# Step 1: Ask for the user name:
def askName():
    name = input(Fore.YELLOW + "\nAGENT CODE:\n")
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


