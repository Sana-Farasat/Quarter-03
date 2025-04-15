from termcolor import colored

print(colored("\n\t\t\t ***Cli Based Simple Calculator***\n", "yellow"))

#Taking input from user
num01= int(input(colored("Enter your first number: ", "blue")))
num02= int(input(colored("Enter your second number: ", "blue")))

#Display Operators
print((colored("Enter operator from these: ", "green")))
print(colored("+", "yellow"))
print(colored("-", "yellow"))
print(colored("*", "yellow"))
print(colored("//", "yellow"))
print(colored("**", "yellow"))
print(colored("%", "yellow"))

#Taking operator from user by showing operators list above
operator= input(colored("Enter operator: ", "blue"))

# Defining conditions for operations
if operator == "+":
    result = num01 + num02
    print(colored(f"Your addition answer is {result}", "green"))
elif operator == "-":
    result = num01 - num02
    print(colored(f"Your subtraction answer is {result}", "green"))
elif operator == "*":
    result = num01 * num02
    print(colored(f"Your multiplication answer is {result}", "green"))
elif operator == "//":
    result = num01 // num02
    print(colored(f"Your division answer is {result}", "green"))
elif operator == "**":
    result = num01 ** num02
    print(colored(f"Your exponent answer is {result}", "green"))
elif operator == "%":
    result = num01 % num02
    print(colored(f"Your modulus answer is {result}", "green"))
else:
    print(colored("Invalid operation..", "red"))