"""
This program is a guessing game between the computer and a user. 
It uses the python module "random" to generate a random number
the user or the computer has to guess.
"""

import random


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
         
    msg = """
    Congratulations!
    You guessed the correct number.
    """
    print(msg)
    return puzzle(10)
#output_user = puzzle(10)



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
    
    print(msg_2)
    return computer_logic(10)
#output_computer = computer_logic(10)

#Retrieves game option from user.
MAIL = """
Which game would you like to play?
Enter 'user guess', 'computer guess' or 'q' to quit.
"""
option = ''
while option != "user guess" or "computer guess" or "q":
    option = input(MAIL)

    if option == 'user guess':
        #puzzle(10)
        output_user = puzzle(10)
        print(output_user)

    elif option == 'computer guess':
        #computer_logic(10)
        output_computer = computer_logic(10)
        print(output_computer)
else:
    if option == 'q':
        print('Game Over')
