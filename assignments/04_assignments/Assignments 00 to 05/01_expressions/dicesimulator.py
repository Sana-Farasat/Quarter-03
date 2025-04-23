# Import random module
import random

print("*****DiceSimulator Program*****")

"""
Simulate rolling two dice, three times.  Prints the results of each die roll.  This program is used
to show how variable scope works.
"""

DICE_NUM_SIDES = 6   # Global scope variable


# Function One
def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, DICE_NUM_SIDES) # Local scope variable
    die2: int = random.randint(1, DICE_NUM_SIDES) # Local scope variable
    total: int = die1 + die2
    print("Total of two dice:", total)

# Function Two
def main(): 
    die1: int = 10 # Local scope variable
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))

# Calling main function
main()

"""
Local Scope Variable:
              A variable defined inside a function or block, access only within that function or block.

Global Scope Variable:
                  A variable defined outside any function, accessible throughout the entire program.
"""

