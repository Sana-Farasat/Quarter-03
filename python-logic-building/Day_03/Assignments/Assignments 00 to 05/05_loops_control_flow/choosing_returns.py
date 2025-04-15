"""
Guess My Number
"""

import random

def guess_my_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = input("Enter your guess (1-100): ")

            if user_guess == "":
                print("Exiting the game.")
                break

            user_guess = int(user_guess)
            attempts += 1

            if user_guess < secret_number:
                print("Your guess is too low!")
            elif user_guess > secret_number:
                print("Your guess is too high!")
            else:
                print(f"🎉 Congratulations! You guessed it right in {attempts} attempts. The number was {secret_number}.")
                break

        except ValueError:
            print("Please enter a valid number!")

def main():
    print("🎮 Welcome to the Guess My Number Game!")
    guess_my_number()

main()
