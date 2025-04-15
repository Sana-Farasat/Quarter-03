"""
Fill out the get_name() function to return your name as a string! We've written a main() function for you which calls your function to retrieve your name and then prints it in a greeting.
"""

#Function to return name as a string
def get_name(name):
    NAME = f"Hi {name}!"
    return NAME

#Main function
def main():
    PROMPT = input("Enter your good name: ")
    respone = get_name(PROMPT).title()
    print(respone)

#Call the function
main()

