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



# Answer 1
def getTarget():
    print('\nYour next target is PROFILE\n')
    continueSession()

# Answer 2
def getCar():
    print('\nYou parked your car at your local Supermarket\n')
    continueSession()

# Answer 3
def getTreat():
    print('\nSomething from Q-Branch\n')
    continueSession()


# All Options
def showQuestions():
    options = ["1. Who is my next Target", "2. Where is my closest car", "3. I need a treat from Q-Branch", "4. End session"]
    for x in options:
        print(x+"")

# Step 1: Ask for the user name:
def askName():
    name = input("Please enter your Agent Code: ")
    if name == "007":
        print(greeting+" "+name+", Your session is logged at: " +start_time+".\n")
        showQuestions()
    elif name == "47":
        print(greeting+" "+name+", Your session is logged at: " +start_time+".\n")
        showQuestions()
    elif name == "":
        print("Your session cannot be started, please enter a valid Agent Code!")
        askName()
    else:
        print("Your session cannot be started")
        askName()

askName()


# Question response:
user_input = ''

while True:
    user_input = int(input('\nPlease enter option: '))
    if user_input == 1:
        getTarget()
        continue
    elif user_input == 2:
        getCar()
        continue
    elif user_input == 3:
        getTreat()
        continue
    elif user_input == 4:
        print('\nSession ended\n')
        break
    else:
        print('Type a number 1-4 please')
        continue

