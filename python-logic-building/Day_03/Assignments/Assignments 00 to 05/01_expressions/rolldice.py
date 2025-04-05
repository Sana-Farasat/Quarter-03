"""
Simulate rolling two dice............
"""

# Import the random library to simulate the random things like dice 
import random

# Total sides of the dice
DICE_SIDES = 6

def main():

    # Roll die
    DICE_1 = random.randint(1 , DICE_SIDES)
    DICE_2 = random.randint(1 , DICE_SIDES)

    # Total of two dices
    TOTAL = DICE_1 + DICE_2

    # Print out the results
    print("Dice have", DICE_SIDES, "sides each.")
    print("First die:", DICE_1)
    print("Second die:", DICE_2)
    print("Total of two dice:", TOTAL)

if __name__ == '__main__':
    main()