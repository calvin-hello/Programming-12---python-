"""
A python quiz game.
"""

def quiz():
    score = 0
    #Question 1
    answer = input("what does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    #Question 2
    answer = input("what does GUI stand for? ")
    if answer.lower() == "graphic user interface":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    #Question 3
    answer = input("what does API stand for? ")
    if answer.lower() == "application programmable interface":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    #Question 4
    answer = input("what does https stand for? ")
    if answer.lower() == "hypertext transfer protocol secure":
        print("Correct!")
    else:
        print("Incorrect!")

    #Question 5
    answer = input("what does html stand for? ")
    if answer.lower() == "hypertext mark up language":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    
    #Question 6
    answer = input("what does os stand for? ")
    if answer.lower() == "operating system":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    #Question 7
    answer = input("What is a programming language?\n")
    if "instruction" or "computer" or "algorithm" or "data structures" in answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    #Question 8
    #formula = "area = length * width"
    answer = int(input("Calculate the area of a mall with length 50cm and width 30cm.\n"))
    if  answer == 1500:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    #Question 9
    answer = input("What is an html tag\n")
    if ("building block" or "layout" or "webpage" in answer) and len(answer) > 10:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    #Question 10
    answer = input("What events are used to make a webpage interractive?\n")
    if answer == "DOM" or "Dom" or "dom":
        print("Correct!")
        score += 0.5
    elif answer == "Document Object Model" or "document object model":
        print("Correct")
        score += 1
    else:
        print("Incorrect!")
    #Displaying the score.
    print("Your score:" + str(score))
    print("Your percentage: " + str((score / 10) * 100) + " %")

#Greeting the user.
print("Welcome\nThis is a computer quiz game.")

playing = input("Do you want to play? ")
#Keeping track of the score


if playing.lower() != "yes":
    quit()

print("Okay! Let's play")
quiz()


#REPLAY
replay = input("Would you like to play again? ").lower()
if replay == "yes":
    quiz()
else:
    print("Thanks for your feedback.")
    quit()

