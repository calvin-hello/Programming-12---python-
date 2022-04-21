"""
An adventure game.
"""
#IMPORTING IMAGE FROM THE IMAGE MODULE.
from PIL import Image

def adventure():
    answer = input("You are on a dirty road, it has come to an end and you can go left or right. Which path would you take. Type 'left' or 'right.'").lower()

    if answer == "left":
        answer = input("You've come to a river and you can walk on it or swim around it. Type 'walk' or 'swim.'").lower()
        #IMAGE FOR RIVER.
        img_riv = Image.open("river.jpg")
        img_riv.show("river.jpg")
        if answer == "swim":
            print("You swam and was swallowed by an anconda.")
        elif answer == "walk":
            print("You tried to defy gravity and died as a result of your curiosity.")

    elif answer == "right":
        answer = input("You've come to a bridge. Do you want to cross it or head back (cross/back).").lower()
        if answer == "back":
            print("You turned around because of fear. There is no room for cowardice.")
        elif answer == "cross":
            answer = input("You crossed and saw a monkey traped.\nDo you rescue it or do you abandon it to its mysery?(rescue/abandon)\n")
            if answer == "rescue":
                print("You were rewarded the Northeastern medalion by the Guardian of the West.\nYour adventure ends here!")
                #IMAGE FOR MEDALLION
                img_med = Image.open("medallion.jpg")
                img_med.show("medallion.jpg")
            elif answer == "abandon":
                print("You were punished for your sins and selfishness.\nYou lose!")
        else: 
            print("See you in the next adventure.")
    else:
        print("Option is not valid. You lose!")

    #Image that congratulates traveler for their attempts.
    img_br = Image.open("brave.jpg")
    img_br.show("brave.jpg")

#Game commencement
name = input("Your Name: ")
print(f"Welcome {name}.\nYour adventure begins here!")
#Image of an adventure poster.
ad_img = Image.open("advent.jpg")
ad_img.show("advent.jpg")

response = input("Would you rise to your feet and accept the quest that waits?(I accept the quest/ I refuse the quest) ")
if response == "I accept the quest":
    adventure()

elif response == "I refuse the quest":
    print("Such cowardice.\nDepart from here!")
    quit()