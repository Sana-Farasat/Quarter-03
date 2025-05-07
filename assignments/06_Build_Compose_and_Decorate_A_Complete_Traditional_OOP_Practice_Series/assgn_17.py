# Class Decorators
"""
Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.
"""

# Class Decorator
"""
Just like function decorators modify functions, class decorators modify or extend classes.
They take a class as input and return a new or modified class.
"""
# Class decorator
def add_greeting(cls):
    # Add a new method to the class
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Dynamically add method to the class
    return cls  # Return modified class

# Apply class decorator
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Test the decorated class
p = Person("Amit")
print(p.greet())  # Output: Hello from Decorator!

"""
@add_greeting takes Person class and adds a new method greet() to it.

Now Person objects can call .greet(), even though it wasn’t originally in the class.
"""