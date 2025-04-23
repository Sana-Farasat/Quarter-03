"""
We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

What's your name? Sophia

Greetings Sophia!
"""

def Greet(name):
    
    return f"Hey {name}!"

def main():
    user_input = input("What's your good name? ")
    print(Greet(user_input))

main()
    