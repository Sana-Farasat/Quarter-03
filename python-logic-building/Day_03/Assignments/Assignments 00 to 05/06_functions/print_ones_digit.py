"""
Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

Enter a number: 42 The ones digit is 2
"""
#Function for ones_digit
def print_ones_digit(num): 
    print("The ones digit is", num % 10) # % 10 helps us get the last digit of any number.

#Main function
def main(): 
    num = int(input("Enter a number: ")) 
    print_ones_digit(num)

#Call the function
main()