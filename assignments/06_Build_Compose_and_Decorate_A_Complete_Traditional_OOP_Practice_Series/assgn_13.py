# Composition
"""
Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.
"""

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car ke andar Engine ka object banaya

    def start_car(self):
        return self.engine.start()  # Car Engine ka method use kar rahi hai

# Use
car = Car()
print(car.start_car())
