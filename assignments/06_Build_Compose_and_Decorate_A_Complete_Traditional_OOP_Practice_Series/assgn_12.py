# Static Methods
"""
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.
"""

class TemperatureConverter():

    @staticmethod
    def celcius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
print(TemperatureConverter.celsius_to_fahrenheit(0))    # Output: 32.0
print(TemperatureConverter.celsius_to_fahrenheit(100))  # Output: 212.0
