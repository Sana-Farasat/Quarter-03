import random

choices : list = ["rock" , "paper" , "scissor"] # choices stored in lowercase

while True:
    user_choice = input("Choose Rock, Paper or Scissor: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please enter only Rock, Paper or Scissor! ❌")
        continue

    computer_choice = random.choice(choices)  # use choice, not choices

    print(f"Computer chose: {computer_choice.capitalize()}")  # Show it pretty

    if user_choice == computer_choice:
        print("It's a tie! 🤝")
    elif user_choice == "rock":
        if computer_choice == "scissor":
            print("You Won! 🎉")
        else:
            print("You Lost! 😢")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You Won! 🎉")
        else:
            print("You Lost! 😢")
    elif user_choice == "scissor":
        if computer_choice == "paper":
            print("You Won! 🎉")
        else:
            print("You Lost! 😢")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break





