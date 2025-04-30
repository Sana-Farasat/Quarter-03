# Public Variables and Methods
"""
Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.
"""

class Car():
    def __init__(self, brand):
        self.brand = brand  # public variable

    def start(self):   # public method
        print(f"I got {self.brand} car from my office.")

car = Car("Totoya")
print(car.brand)  # Method 1
car.start()    # Method 2