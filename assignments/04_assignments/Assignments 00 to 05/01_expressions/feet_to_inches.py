"""
Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.
"""

INCHES = 12

#Function to convert feet into inches
def Conversion(f):
    feet : int = f * INCHES # Conversion formula
    return feet

# Input from the user, converted to float
user_input = float(input("Enter number of feet: "))

# Call the function with an arguement
result :float = Conversion(user_input)

print(str(user_input) + " feet = " + str(result) + " inches ")


