#Rock-Paper-Scissors game
from random import randint
from time import sleep
options = ["R", "P", "S"]
user_message = "You lost!"
user_message2 = "You win!"
# Function that defines who is a winner
def decide_winner(user_choice, computer_choice):
    print "User's choice %s" % (user_choice)
    print "Computer selecting..."
    sleep(1)
    print "Computer's choice %s" % (computer_choice) 
    user_choice_index = options.index(user_choice)
    #computer_choice_index = options.index(computer_choice)
    if user_choice_index == computer_choice:
        print "It's a tie!"
    elif user_choice_index == options[0] and computer_choice == options[2]:
        print "%s"% (user_message)
    elif user_choice_index == options[1] and computer_choice == options[0]:
        print "%s"% (user_message)   
    elif user_choice_index == options[2] and computer_choice == options[1]:   
        print "%s"% (user_message)  
    elif user_choice_index >2:
        print "It's a garbage!"
        return
    else:
        print "%s"% (user_message2)  
       
#Function that starts a game
def play_RPS():
    print "The game Rock-Paper-Scissors starts..."  
user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors:")
sleep(1)
user_choice.upper()
computer_choice = randint(0, len(options)-1)

play_RPS()
decide_winner(user_choice, computer_choice)