"""
The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

-----------------------------------------------------------------------

For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

BC ** 2 = AB ** 2 + AC ** 2
"""

# Import math library for using square function
import math 

def main():

    # Taking input from users to get two side length of the triangle
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse by using two sides
    bc: float = math.sqrt(ab**2 + ac**2)
    rounded_bc = math.floor(bc)

    print("The length of BC (the hypotenuse) is: " + str(rounded_bc))

if __name__ == '__main__':
    main()


