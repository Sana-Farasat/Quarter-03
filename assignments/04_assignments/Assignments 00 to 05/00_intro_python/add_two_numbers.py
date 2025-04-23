# Taking input from users to sum
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

# Calculating 
sum = first_num + second_num
print(f"The total sum is {sum}")

#---------------------------------------------------------

# Function for sum
def sum():
    try:
        first_num = int(input("Enter first number: "))
        second_num = int(input("Enter second number: "))
        sum = first_num + second_num
        print(f"The total sum is {sum}")
    except ValueError:
        print("Invalid input! Please enter number only..")

sum()


    