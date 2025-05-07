# Function Decorators
"""
Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().
"""

# Decorator Def
"""
A decorator is a function that wraps another function to extend its behavior without modifying the original function code.

Decorator ek function hota hai jo kisi doosre function ke upar kaam karta hai — bina us function ko badle.

Yeh function ke behaviour ko enhance karta hai — jaise function chalne se pehle ya baad me kuch extra kaam karwana
"""

# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()  # Call the original function
    return wrapper

# Apply decorator using @ syntax
@log_function_call
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
