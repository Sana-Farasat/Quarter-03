# Importing module
import random

# Generating and printing 10 random numbers between 1 and 100
for _ in range(10):
    print(random.randint(1, 100), end=" ")

"""
-In Python, the underscore (_) is used as a convention to indicate that a variable's value is intentionally unused or not needed.
-random.randint(1, 100) generates a random integer between 1 and 100, inclusive.
-The for _ in range(10) loop runs 10 times, each time printing a random number.
-end=" " ensures that the numbers are printed on the same line with a space between them.
"""