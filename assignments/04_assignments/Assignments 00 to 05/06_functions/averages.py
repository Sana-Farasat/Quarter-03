"""
Write a function that takes two numbers and finds the average between the two.
"""

#Function to calculate average
def Average(num1 , num2):
    ave = (num1 + num2) / 2
    return ave

#Function to take input from user
def Prompt():
    prompt1 = int(input("Enter your first number: "))
    prompt2 = int(input("Enter your second number: "))
    result = Average(prompt1 , prompt2)
    print(f" \n The average is {result} \n ")

#Call teh function
Prompt()