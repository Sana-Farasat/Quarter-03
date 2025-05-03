# Abstract Classes and Methods
"""
Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().
"""

# Abstract Class Definition
"""
An abstract class is a class that cannot be instantiated directly and is designed to be inherited by other classes.

It may contain abstract methods (methods without body), which must be implemented by any subclass.
"""

# Key Features of Abstract Class
"""
Cannot be Instantiated:
--> Abstract class ka direct object nahi banaya ja sakta.

Used for Inheritance:
--> Ye class sirf inherit ki jati hai, aur subclasses ko compulsory kuch methods implement karne padte hain.

Abstract Methods:
--> Aise methods jinka sirf naam hota hai, body nahi hoti.
--> Subclasses ko override karna padta hai.

Can Have Normal Methods Too:
--> Abstract class me abstract ke sath-sath normal (fully defined) methods bhi ho sakte hain.

Helps in Polymorphism:
--> Multiple subclasses ko ek hi type ke roop me treat karne me madad karta hai.

Acts as a Blueprint:
--> Ye ek template/blueprint ki tarah kaam karti hai, jisse subclasses design ki jati hain.

"""

from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract Class
    @abstractmethod
    def area(self):  # Abstract Method
        pass   

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
rectangle = Rectangle(3, 6)
print(f"Area of rectangle: {rectangle.area()}")