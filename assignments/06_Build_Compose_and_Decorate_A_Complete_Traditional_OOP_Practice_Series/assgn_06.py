# Constructors and Destructors
"""
Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).
"""

class Logger():
    def __init__(self):
        print("Message Before: Logger object created..")

    def __del__(self):
        print("Message After: Logger object deconstructor..")

log = Logger()

del log