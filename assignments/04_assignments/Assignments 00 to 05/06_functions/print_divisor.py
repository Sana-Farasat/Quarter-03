"""
Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division).

Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12
"""

#Function to take all divisors
def Divisors(num : int):
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1 #i + 1 isliye likha hai taake counting 1 se start ho (0 se nahi, kyunki 0 se divide karna error deta hai).
        if num % curr_divisor == 0:
            print(curr_divisor)

#Main function
def main():
    num = int(input("Enter a number: "))
    Divisors(num)

#Call the function
main()

