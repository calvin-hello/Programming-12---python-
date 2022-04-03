"""
This program is a guessing game between the computer and a user. 
It uses the python module "random" to generate a random number
the user or the computer has to guess.
"""

import random
COUNT = 0

#COMPUTER GUESS.
#User guesses computer's secret number.
def puzzle(num) -> str:
    probability: int = random.randint(1, num)
    #While loop for general decision making.
    user_number = 0
    while user_number != probability:
        #Retrieving user's guess.
        user_number = int(input(f"Guess a number between 1 and {num}: "))
        if user_number < probability:
            print("Too Low!")
        elif user_number > probability:
            print("Too High!")

    msg = f"""
    Congratulations!
    You guessed the correct number.
    You won {COUNT} times.
    """

    #print(msg)
    return msg
    #return 10




#USER GUESS.
#User guesses computers secret number.
def computer_logic(x) -> str:
    min = 1
    max = x
    statement = ''
    while statement != 'c':
        if min != max:
            lucky_number = random.randint(min, max)
        else:
            lucky_number = min
        statement = input(f'Is {lucky_number} too high (h), too low (l), or correct (c)? ')
        if statement == 'h':
            max = lucky_number - 1
        elif statement == 'l':
            min = lucky_number + 1
    
    msg_2: str = f'''
    Hi I am Jarvis the computer!
    I guessed your number, {lucky_number}, correctly!
        AWESOME!!
    '''
    #print(msg_2)
    return msg_2
    #return 10



def execute():
    #Retrieves game option from user.
    MAIL = """
    Which game would you like to play?
    Enter 'user guess', 'computer guess' or 'q' to quit.
    """
    option_1 = "computer guess"
    option_2 = "user guess"
    exit = "q"

    opt_lis = [option_1, option_2, exit]

    #user_data = input(MAIL)
    user_data = " "
    #wrong_input = True

    #Code is almost complete. 
    #The challenge with the code is the inability of the while loop to != two or more strings.
    #It won't function properly that way, unless it is equal to only one string.
    '''
    while  wrong_input == False:
        user_data = input(MAIL)
    
        if user_data != option_1:
            user_data = input(MAIL)
        elif user_data != option_2:
            user_data = input(MAIL)
        elif user_data != exit:
            user_data = input(MAIL)
    '''
    while user_data != opt_lis:
        user_data = input(MAIL)

        if user_data == "computer guess":
            output_computer = computer_logic(10)
            #print(output_computer)
            return output_computer
        elif user_data == "user guess":
            output_user = puzzle(10)
            #print(output_user)
            return output_user
        elif user_data == "q":
            #print("Game Over!")
            return "Game Over!" 
        continue
    
    #print("Game over!")
    


result = execute()
print(result)

#PROGRAMMING CAN BE HARD - THAT'S TRUE AND I AGREE.
#IT CAN BE BORING, STRESSFUL OR FRUSTRATING IF  YOU JUST CAN'T SOLVE A PROBLEM
#AFTER 3 HOURS. IT MAY SOMETIMES SEEM IMPRUDENT, THUS YOU SPEND DAYS TO SOLVE A
#MINOR PROBLEM. TO HAVE FUN WITH PROGRAMMING YOU HAVE TO DEVELOP PASSION AND
#STRONG RESILIENCE FOR IT.
#I LACKED THIS AT FIRST. THIS MADE MY PROGRAMMING JOURNEY TOUGH - LEADING TO MY 
#DYING INTEREST IN PROGRAMMING. HOWEVER, DUE TO THE PROGRESS OF MY FRIEND - 
#FULFILLING THE BIBLE SCRIPTURES: "IRON SHARPENETH IRON, SO SHALL A MAN SHARPEN THE COUNTENANCE
# OF HIS FRIEND - PROVERBS 27:17" AND "...PROVOKE ONE ANOTHER UNTO GOOD WORKS."
#A STRUCK OF PASSION AFFECTED ME, RESULTING IN MY QUEST FOR GREAT HEIGHTS IN SOFTWARE ENGINEERING.

#Using while loop to repeat question until data entered = values required.


#print(result)

#Can use the code below to work on the count for rock paper scissors game.
"""
counter = 1 
while (counter <= 5): 
    if counter < 2:
        print("Less than 2")
    elif counter > 4:
        print("Greater than 4")
    counter += 1
"""