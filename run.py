import datetime

# Session Management
def continueSession():
    qbranch = ''
    while True:
        qbranch = input("Would you like to continue? [Y/N]: ")
        if qbranch == 'Y':
            showQuestions()
            continue
        elif qbranch == 'N':
            print("\nYour session has be terminated!\n")
            break
        else:
            print("Please only enter Y for 'yes' or N for 'no'")
            showQuestions()
            continue

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

# Step 1: Ask for the user name:
def askName():
    name = input("Please enter your Agent designation: ")
    if name == "007":
        print(greeting+" "+name+", Your session is logged at: " +start_time+".\n")
    elif name == "Agent 47":
        print(greeting+" "+name+", Your session is logged at: " +start_time+".\n")
    else:
        print("Your session cannot be started")

askName()

# Answer 1
def getTarget():
    print('Your next target is PROFILE')

# Answer 2
def getCar():
    print('You parked your car at your local Supermarket')

# Answer 3
def getTreat():
    print('Something from Q-Branch')

# All Options
def showQuestions():
    options = ["1. Who is my next Target", "2. Where is my closest car", "3. I need a treat from Q-Branch", "4. End session"]
    for x in options:
        print(x+"\n")

showQuestions()


# Question response:
user_input = ''

while True:
    user_input = input('Please enter option: ')
    if user_input == '1':
        print('You picked JavaScript')
        continueSession()
        break
    elif user_input == '2':
        getCar()
        continueSession()
        break
    elif user_input == '3':
        print('You picked TypeScript')
        continueSession()
        break
    elif user_input == '4':
        print('Session ended')
        break
    else:
        print('Type a number 1-4 please')
        continue
    