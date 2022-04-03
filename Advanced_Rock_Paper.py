'''
Advanced rock, paper, scissors ...
Game Name: Rock paper scissors spock lizard
'''
import random

#Main function that contains code.
def game():
    #Output msg that retrieves user's option.
    
    gamer = input("Rock (r), paper (p), scissors (x), spock (s) or lizard (l)? ")
    #Computer's move
    host = random.choice(['r','p', 'x', 's', 'l'])

    if gamer == host:
        return "It's a tie"
      
    if win(gamer, host):
        return "You won!"

    return "You lost :("

def win(player, machine):
    # Formula to win
    # p > r, r > x, s > x, l > x
    if (player == 'p' and machine == 'r') or (player == 'r' and machine == 'x') \
         or (player == 's' and machine == 'x') or (player == 'l' and machine == 'x'):
         return True   

#Commences game.
print(game())
    