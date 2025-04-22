"""
Guess My Number

I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

Enter a new number: 25 Your guess is too low

Enter a new number: 40 Your guess is too low

Enter a new number: 45 Your guess is too low

Enter a new number: 48 Congrats! The number was: 48
"""

import random

def main():
    # Generate the secret number
    secret_number: int = random.randint(0, 10)
    attempts: int = 0

    print("\n 🎯 I am thinking of a number between 0 and 10...")

    while True:
        try:
            guess: int = int(input("🔢 Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("⬆️ Too low!\n")
            elif guess > secret_number:
                print("⬇️ Too high!\n")
            else:
                print(f"🎉 Congrats! You guessed it right. The number was {secret_number}.")
                print(f"🧠 You took {attempts} attempts.")
                break  # Exit the loop when guess is correct

        except ValueError:
            print("❗ Please enter a valid number (digits only).\n")

if __name__ == '__main__':
    main()
