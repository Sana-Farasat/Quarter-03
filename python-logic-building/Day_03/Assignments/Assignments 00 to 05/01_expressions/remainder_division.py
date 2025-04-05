import math

def main():

    input1 = float(input("Please enter an integer to be divided: "))
    input2 = float(input("Please enter an integer to divide by: "))

    division = input1 // input2
    remainder = math.remainder(input1 , input2)

    print(f" \n The result of this division is {division} with a remainder of {remainder} \n ")
    
main()
