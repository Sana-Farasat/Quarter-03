"""
In the Gregorian calendar, three criteria must be checked to identify leap years:

The given year must be evenly divisible by 4;
If the year can also be evenly divided by 100, it is NOT a leap year; unless:
The year is also evenly divisible by 400. Then it is a leap year.
"""


# Function for calculating leap year
def Leap_Year():

    prompt = int(input("Please enter year: "))

    if prompt % 4 == 0 or prompt % 100 == 0 or prompt % 400 == 0:
        print("That's a leap year !")
    else:
        print("That's not a leap year..")

# Calling Function
Leap_Year()