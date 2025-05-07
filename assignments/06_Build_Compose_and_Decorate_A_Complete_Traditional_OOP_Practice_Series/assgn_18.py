# Property Decorators: @property, @setter, and @deleter
"""
Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute

    # Getter for price
    @property
    def price(self):
        print("Getting price...")
        return self._price

    # Setter for price
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            print("Setting price...")
            self._price = value

    # Deleter for price
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Create a Product object
p = Product("Laptop", 1000)

# Get the price using @property
print(p.price)  # Output: Getting price... 1000

# Set the price using @price.setter
p.price = 1200  # Output: Setting price...

# Get the updated price
print(p.price)  # Output: Getting price... 1200

# Try setting a negative price
p.price = -500  # Output: Price cannot be negative!

# Delete the price using @price.deleter
del p.price  # Output: Deleting price...
