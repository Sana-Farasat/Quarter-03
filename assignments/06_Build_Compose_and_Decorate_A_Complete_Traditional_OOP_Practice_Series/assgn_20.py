# Creating a Custom Exception
"""
Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.
"""

# Step 1: Create a custom exception class
class InvalidAgeError(Exception):
    pass  # You can also add custom message here

# Step 2: Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    else:
        print("Access granted.")

# Step 3: Handle the exception with try...except
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print(f"Access denied: {e}")
