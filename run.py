from datetime import datetime
from geopy.geocoders import Nominatim
from colorama import Fore, init
init()


# PROGRAM VARIABLES:


loc = Nominatim(user_agent="GetLoc")  # get address from city name
code_options = ['007', '47', '0']  # Predefined agent code options
current_time = datetime.now().strftime("%H:%M:%S")  # Current Time
if current_time < "12:00:00":
    greeting = "\nGood morning"
elif current_time < "18:00:00":
    greeting = "\nGood afternoon"
else:
    greeting = "\nGood evening"


# PROGRAM FUNCTIONS:


def continue_session():  # Session Management
    qbranch = ''
    while True:
        qbranch = input(Fore.YELLOW + "Continue? [Y/N]:\n").lower()
        if qbranch == 'y':
            show_options()
            continue
        elif qbranch == 'n':
            print(Fore.RED + "\nSession terminated!\n")
            quit()
        else:
            print(Fore.CYAN + "\nPlease only enter Y for 'yes' or N for 'no'\n")
            continue_session()


def answer_one():  # Answer 1
    print(Fore.CYAN + '\nTarget:')
    print(Fore.WHITE + 'Shinji Nakamora')
    print(Fore.CYAN + '\nObjective:')
    print(Fore.WHITE + 'Extraction to Rendezvous')
    print(Fore.CYAN + '\nCurrent Location:')  # calling the Nominatim tool
    get_location = loc.geocode("Paris, France\n")  # entering the location name
    print(Fore.WHITE + get_location.address)  # printing address
    print(Fore.WHITE + "Latitude = ", get_location.latitude, "")  # printing latitude
    print(Fore.WHITE + "Longitude = ", get_location.longitude)  # printing longitude
    print("\n")


def answer_two():  # Answer 2
    print(Fore.CYAN + '\nTravel Arrangements:')
    print(Fore.WHITE + 'Meet with Q at 11:11 tomorrow to pick up your Travel documentation and equipment:\n')
    print(Fore.CYAN + '\nCurrent Location:')
    getLoc = loc.geocode("Dublin Zoo, Dublin, Ireland\n")
    print(Fore.WHITE + getLoc.address)
    print(Fore.WHITE + "Latitude = ", getLoc.latitude, "")
    print(Fore.WHITE + "Longitude = ", getLoc.longitude)
    print(Fore.CYAN + '\nNotes:')
    print(Fore.WHITE + 'Q will be in a purple hoodie outside the Red Panda enclosure!:\n')
    print("\n")
    continue_session()


def mission_accept():
    print(Fore.CYAN + '\nMISSION ACCEPTED!\n')


def mission_reject():
    print(Fore.RED + '\nMISSION REJECTED!\n')


def answer_three():  # Answer 3
    accept_mission = ''
    while True:
        accept_mission = input(Fore.YELLOW + "ACCEPT MISSION? [Y/N]:\n").lower()
        if accept_mission == 'y':
            mission_accept()
            quit()
        elif accept_mission == 'n':
            mission_reject()
            quit()
        else:
            print(Fore.CYAN + "\nPlease only enter Y for 'yes' or N for 'no'\n")
            answer_three()


def option_responses():  # Option responses
    user_input = ''

    while True:
        try:
            user_input = int(input(Fore.YELLOW + '\nENTER NUMBER TO PROCEED [1-4]:\n'))
            if user_input == 1:
                answer_one()
                continue_session()
                continue
            elif user_input == 2:
                answer_two()
                continue
            elif user_input == 3:
                answer_three()
                continue
            elif user_input == 4:
                print(Fore.RED + "\nSession terminated!\n")
                quit()
        except ValueError:
            print('Type any number from 1-4 please')
            continue


def show_options():  # Step 2: All Options
    options = [
        Fore.WHITE + "1. NEXT TARGET",
        "2. TRAVEL ARRANGEMENTS",
        "3. ACCEPT MISSION",
        "4. TERMINATE SESSION"
    ]
    for x in options:
        print(x+"")
    option_responses()


def agent_code():  # Step 1: Ask for the agent code:
    code = input("AGENT CODE:")
    if code in code_options:
        print(
            Fore.GREEN + greeting + " " + code +
            ", Your session is logged at: " + current_time +
            "\n"
        )
        show_options()
    elif code not in code_options:
        print(Fore.RED + "Please enter a valid Agent Code!")
        agent_code()
    else:
        print(Fore.RED + "System Error!")
        agent_code()


agent_code()
