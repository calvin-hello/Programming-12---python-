"""
A modified hangman project.
REFERENCE TO ROCK PAPER SCISSOR GAME ON "GEEKFORGEEKS" TO 
LEARN HOW TO INCLUDE IMAGES IN THE HANGMAN GAME FOR DIFFERENT
SECTIONS OF THE BODY.
"""
#Importing necessary modules.
import random
from hangman_visual import lives_visual_dict
import string
import time
#Data that contains a list of words, 20 in total - a word dictionary.
#This word dictionary should be given a name data.
#Function for valid words accepted by the computer.

#MOD 1 - LIST OF WORDS WITH WORDS TO OMIT.
data = ["apart", "apartment", "Zimmerman", "building", "apologise", "apology",
"appear", "Kwantlen", "appearance", "apple", "application", "bay", "beach",
"bean", "bear", "beat", "beautiful", "beauty", "Rai", "because"]

def valid_data(data):
    word = random.choice(data)


    #MODIFICATION 1
    #List of characters to exclude.
    #Using while loop to omit data (Rai, Zimmerman, Kwantlen)
    while "Rai" in word or "Zimmerman" in word or "Kwantlen" in word:
        word = random.choice(data)

    return word.upper()

#Function hangman.
def hangman():
    word = valid_data(data)
    #Documenting modification in case it causes error.
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    #MODIFICATION 5
    #Mod 5 for set that contains positive msgs using the random module to access its characters
    #when the user enters a letter.
    motivation = [
        "You can do this!", "Don't give up!", "Almost there!", "Just hold on a little longer!", "Keep up the grind!"
    ]
    criticism = [
        "Come on, is that all you've got?", "Boi! Your performance is bad", "What were you thinking bro?", "Are you confused or are you lazy?"
    ]
    #Positive message for correct user guesses.
    valid = random.choice(motivation)
    invalid = random.choice(criticism)

    while len(word_letters) > 0 and lives > 0:
        #MODIFICATION 4 - TIME DELAY.
        time.sleep(1)
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))
        
        #List of what current word is.
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(lives_visual_dict[lives])
        print("Current word: ", " ".join(word_list))
        #Retrieves Input.
        user_character = input("Guess a letter: ").upper()

        #MODIFICATION 5
        if user_character in word_letters:
            print(valid)
        elif user_character not in word_letters:
            print(invalid)

        if user_character in alphabet - used_letters:
            used_letters.add(user_character)
            if user_character in word_letters:
                word_letters.remove(user_character)
            else:
                lives = lives - 1
                #MODIFICATION 4
                time.sleep(1)
                print("Letter is not right")
               
        elif user_character in used_letters:
            print("Word is used. Try again!")
        else:
            print("Invalid input. Try again!")  


    if lives == 0:
        #MODIFICATION 4
        time.sleep(3)
        print(lives_visual_dict[lives])
        print("You died, sorry. The word was", word)
    else:
        time.sleep(1)
        print("You guessed the word", word, "!")
hangman()


#MODIFICATION 3
#OPTION FOR USER TO PLAY GAME AGAIN.
#Funtion 'interest.'
#The purpose of the function is to end the game with 'return'
#if user option == no. Finding it challenging to use 'break'
#there. This may be a result of both 'continue' and 'break' in
# the function. However, I don't think that should affect it.

def interest():
    play_again = " "
    msg = f"""
    Would you like to play again?
    Type 'yes' or 'no':  
    """
    while play_again != "yes" or "no":
        play_again = input(msg)
        if play_again == "yes":
            hangman()
            continue
        elif play_again == "no":
            #print("Game over!")
            #break
            return "Game over!"
        else:
            return "Thanks for the feedback."
#printing the function so that the return statement will appear on console.
display = interest()
print(display)

