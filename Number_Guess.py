#Based on the user's guess, the program should determine a winner. If the user's guess is greater than the total value of the dice roll, they win! Otherwise, the computer wins.
from random import randint
from time import sleep
def get_user_guess():
    """user put a guess number"""
    user_guess = int(raw_input("Guess a number:"))
    return user_guess
def roll_dice(number_of_sides):
    """randomly choosing a number"""
    #define number for first and second roll#
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides*2
    print "Maximum number value is %s" % (max_val)
    sleep(1)
    user_guess = get_user_guess()
    #determine who is winner
    if user_guess > max_val:
        print "You guess is invalid"
        
    else:
      print "Rolling..."
      sleep(2)
      print "%d"% (first_roll)
      sleep(1)
      print "%d"% (second_roll)
      sleep(1)
      total_roll= first_roll +second_roll
      print "%d"%(total_roll)
      print "Result..."
      sleep(1)
      if user_guess>total_roll:
          print "You are won"
          
      else:
          print "You are lost"
          
roll_dice(3)        