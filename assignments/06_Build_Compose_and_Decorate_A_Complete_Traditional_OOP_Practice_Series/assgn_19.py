# callable() and __call__()
"""
Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.
"""

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

# Create an instance with factor 5
m = Multiplier(5)

# Use callable() to check if object is callable
print(callable(m))  # Output: True

# Call the object like a function
result = m(10)  # Equivalent to m.__call__(10)
print(result)   # Output: 50
