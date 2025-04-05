def Calculator(first_num, second_num, operation):
    if operation == "+":
        addition = first_num + second_num 
        print(f"Your addition answer is {addition}")
    elif operation == "-":
        subtraction = first_num - second_num
        print(f"Your subtraction answer is {subtraction}")
    elif operation == "*":
        multiplication = first_num * second_num
        print(f"Your subtraction answer is {multiplication}")
    elif operation == "/":
        division = first_num / second_num
        print(f"Your subtraction answer is {division}")
    elif operation == "**":
        exponent = first_num ** second_num
        print(f"Your subtraction answer is {exponent}")
    elif operation == "%":
        modulus = first_num % second_num
        print(f"Your subtraction answer is {modulus}")

first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))
operator = input("Select any operator: ")

Calculator(first, second, operator)
