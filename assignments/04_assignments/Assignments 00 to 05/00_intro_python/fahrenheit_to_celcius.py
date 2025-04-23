"""
Formula:
degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
"""

# Function for conversion F to C
def Conversion():
    print(" \n ******Fahrenheit to Celcius Conversion Program***** \n")
    prompt = int(input("Enter Fahrenheit to convert into Celcius: "))
    degrees_celsius = (prompt - 32) * 5.0/9.0
    print(f"Temperature: {prompt} F = {degrees_celsius:.2f} C")

#Calling function
Conversion()