import random

condition = True

while condition:

    print("\n 🎯 Number Guessing Game (User)")
    print("Please guess any number between 1 and 10 🎰 \n")
   
    try:
      computer_secret = random.randint(1, 10)

      user_guess = int(input("🔢 Please guess any number: "))

      print(f"🤖 Computer Secret number is {computer_secret}")

    except ValueError:
       print("❌ Invalid input..!")
       break
 
    if computer_secret > user_guess:
       print("⬇️ Oops! You guessed smaller number! \n")
    elif computer_secret < user_guess:
       print("⬇️ Oops! You guessed bigger number! \n")
    else:
       print("🎉 Yay ! You guessed right number..")
       break

    play_again = input("Do you want to play again (yes/no): ").lower()

    if play_again in ['yes','y']:
       continue
    else:
       print("👋 Thanks for playing !")
       print("💫----------------------💫")
       break
       
       




    