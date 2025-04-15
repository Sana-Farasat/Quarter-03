"""
Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.
"""

#Function to get double num
def Double_Num(num):
    NUMBER = num * 2
    return NUMBER

#Main Function
def main():
    PROMPT = int(input("Enter your number: "))
    result = Double_Num(PROMPT)
    print(result)

#Call the function
main()
