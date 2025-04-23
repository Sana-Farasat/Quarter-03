"""
Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

Please type a message: Hello! Enter a number of times to repeat your message: 6 Hello! Hello! Hello! Hello! Hello! Hello!
"""

#Function to take message and number from user
def Multiple_Print(message, num):
    for i in range(num):
        print(message)

#Function to take input from user
def main():
    user_message = input("Enter your message: ")
    user_number = int(input("Enter number to print message: "))
    Multiple_Print(user_message, user_number)

#Call the function
main()

