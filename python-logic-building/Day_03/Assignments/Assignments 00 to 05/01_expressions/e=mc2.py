"""
Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
      E = m * c**2
"""

# Function to calculate energy by using Einstein's formula
def Calculate_Energy(m):

   C : int = 299792458
   E = m * C ** 2
   return E

mass : float = float(input("Enter mass (in kg): "))

result : float = Calculate_Energy(mass)

print(f"{mass} kg mass = {result} joules of energy")