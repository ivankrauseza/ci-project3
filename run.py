import datetime

current_time = datetime.datetime.now().time()
morning_start = datetime.time(6, 0)
afternoon_start = datetime.time(12, 0)
evening_start = datetime.time(18, 0)
start_time = current_time.strftime("%H:%M:%S")

if morning_start <= current_time < afternoon_start:
    greeting = "Good morning"
elif afternoon_start <= current_time < evening_start:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

# ENTER YOUR NAME
def askName():
    name = input("Please enter your Agent designation: ")
    if name == "007":
        print(greeting+" "+name+", Your session is logged at: " +start_time+".\n")
    elif name == "Agent 47":
        print(greeting+" "+name+", Your session is logged at: " +start_time+".\n")
    else:
        print("Your session cannot be started")
        
askName()

user_input = ''

while True:
    user_input = input(
        'Pick one: 1) Python | 2) JavaScript | 3) TypeScript [1/2/3]? ')

    if user_input == '1':
        print('You picked Python')
        break
    elif user_input == '2':
        print('You picked JavaScript')
        break
    elif user_input == '3':
        print('You picked TypeScript')
        break

    else:
        print('Type a number 1-3')
        continue


