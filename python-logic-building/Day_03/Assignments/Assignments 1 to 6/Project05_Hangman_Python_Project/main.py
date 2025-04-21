import random

WORD_LIST : list = ["python" , "github" , "nextjs"]
WORD : str = random.choice(WORD_LIST)
GUESS_LETTERS = set()
ATTEMPTS = 7

def DISPLAY_WORD(word, guess_letters):
    display = ""
    for letter in word:
        if letter in guess_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


while ATTEMPTS > 0:
    print("\n\t***Welcome to Hangman Game***")
    print("\t------------------------------")
    print(f"Word: {DISPLAY_WORD(WORD , GUESS_LETTERS)} ")
    print(f"Guess letter: {GUESS_LETTERS} ")
    print(f"Attempts left: {ATTEMPTS}")

    GUESS = input("Enter your guess letter: ").lower()

    # If already guessed
    if GUESS in GUESS_LETTERS:
        print("You already guessed that letter.")
        continue

    GUESS_LETTERS.add(GUESS)

    # Check if guess is wrong
    if GUESS not in WORD:
        ATTEMPTS -= 1
        print(f"Wrong guess! '{GUESS}' is not in the word.")

    # Check if the word is fully guessed
    if set(WORD).issubset(GUESS_LETTERS):
        print(f"\n🎉 Congrats! You guessed the word: {WORD}")
        break

# If attempts ran out
    else:
        print(f"\n💀 Game Over! The correct word was: {WORD}")# If already guessed
   