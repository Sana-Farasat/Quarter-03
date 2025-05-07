# Make a Custom Class Iterable
"""
Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.
"""

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Signals the end of iteration
        value = self.current
        self.current -= 1
        return value

# Using the Countdown class in a for loop
for num in Countdown(5):
    print(num)

# Code Explaination
"""
-Create a class Countdown(start)
-It should count down to 0 when used in a for loop
-Implement:
        __iter__() – returns the iterator (usually self)
        __next__() – returns next value, stops at 0

__iter__() → returns the iterator object (often self).
__next__() → returns the next value each time next() is called.
When countdown goes below 0, it raises StopIteration to stop the loop.
"""