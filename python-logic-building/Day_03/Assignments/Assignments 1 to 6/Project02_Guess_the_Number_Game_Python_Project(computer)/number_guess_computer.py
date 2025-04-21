import random

while True:
    print("\n🎯 Number Guessing Game (Computer)")
    print("Guess any number between 1 and 100 🎰\n")

    try:
        user_input = int(input("🔐 Enter your secret number (Computer will try to guess it): "))
        if user_input < 1 or user_input > 100:
            print("⚠️ Please enter a number between 1 and 100!")
            continue
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        continue

    computer_number = random.randint(1, 100)
    print(f"🤖 Computer guessed: {computer_number}")

    if computer_number > user_input:
        print("📈 Computer's guess is **higher** than your number!")
    elif computer_number < user_input:
        print("📉 Computer's guess is **lower** than your number!")
    else:
        print("🎉 Yay! Computer guessed it right!")

    play_again = input("\n🔁 Do you want to play again? (yes/no): ").lower()

    if play_again in ["yes", "y"]:
        continue
    else:
        print("👋 Thanks for playing! See you next time!")
        print("--------------------------------------------------")
        break
    