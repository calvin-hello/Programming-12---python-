""" 
Madlibs game that consists of three stories. 
It firsts askes the user to choose a story option out of three options.
User has the option to quit by pressing the "q" key.
"""

#Story one
def option_one():
    #Retrieving data from user.
    noun = input("Enter noun: ")
    adj = input("Enter adjective: ")
    plu_noun = input("Enter plural noun: ")
    pod = input("Part of body: ")
    pla = input("Place: ")
    veb = input("Verb ending in -ing: ")

    sty_one = f"{noun} is {adj} he saved the {plu_noun} from the villains of {pla} and got hurt on his {pod}.\
    {noun} also prevented the bad guys from {veb} the water supply. This made the {plu_noun} of {pla} excited -\
    raising their moving their injured {pod} as a sign of perseverance and appreciation."

    return sty_one

#Story two
def option_two():
    #Retrieving data from user.
    noun = input("Enter noun: ")
    adj = input("Enter adjective: ")
    plu_noun = input("Enter plural noun: ")
    pod = input("Part of body: ")
    pla = input("Place: ")
    veb = input("Verb ending in -ing: ")

    sty_two = f"The {adj} black {noun} dives over the mighty eagle. The incident causes the eagle's {plu_noun} to \
    bump their {pod} - {veb} into a deep pit. The eagle dives down the pit to save her {plu_noun} and take them to the {pla}.\
    Ensuring the safety of her {plu_noun}, she leaves, find thorns to barricade her {pla}. The {noun} attempts to hurt the \
    {plu_noun} in the eagle's abscence. However, it is struck on its {pod} by the thorns the surrounds the {pla}. The injured\
    {noun} is brought down to its death."

    return sty_two

#Story three
def option_three():
    #Retrieving data from user.
    noun = input("Enter noun: ")
    adj = input("Enter adjective: ")
    plu_noun = input("Enter plural noun: ")
    pod = input("Part of body: ")
    pla = input("Place: ")
    veb = input("Verb ending in -ing: ")

    sty_three = "{noun} is in grade 12 and enthusiastic to graduate. He there studies through the night to meet {pla}\
    requirements. His mother tells him {veb} early and moderately is good for his health; however, he would not listen.\
    This results in {pod} failure - resulting in his down fall. He is {adj} rushed to the hospital. The {plu_noun} examines \
    {noun} and cautions him that {veb} late for a continuous period of time could lead to his demise."

    return sty_three

#Retrieving user's option.
option = input("Which story would you like play? Enter number: ")

#Using if-else chains 
if option == str(1):
    print(option_one())
elif option == str(2):
    print(option_two())
elif option == str(3):
    print(option_three())
else:
    if option == "q" or "Q":
        print("Game Over!")

#Using while loop to repeat option if user data not equal to required accessing data.
msg_err = """
Invalid input!
Try again.
"""
while option != str(1) or str(2) or str(3) or "q":
    print(msg_err)
    option = input("Which story would you like play? Enter number: ")
    


