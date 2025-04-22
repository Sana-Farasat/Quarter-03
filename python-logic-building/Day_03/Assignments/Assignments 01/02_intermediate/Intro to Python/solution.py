# Milestone 01:

# Step 1: User will enter their weight on Earth
#earth_weight = float(input("Enter a weight on Earth: "))

# Step 2: Calculate Mars weight using the given percentage (37.8%)
#mars_weight = earth_weight * 0.378

# Step 3: Round off the answer to 2 decimal places
#mars_weight = round(mars_weight, 2)

# Step 4: Print the result
#print("The equivalent on Mars:", mars_weight)

# Milestone 02:

# Step 1: Ask for Earth weight
earth_weight = float(input("Enter a weight on Earth: "))

# Step 2: Ask for the name of the planet
planet = input("Enter a planet: ").lower()

# Step 3: Use if-elif to check which planet was entered
if planet == "mercury":
    factor = 0.376
elif planet == "venus":
    factor = 0.889
elif planet == "mars":
    factor = 0.378
elif planet == "jupiter":
    factor = 2.36
elif planet == "saturn":
    factor = 1.081
elif planet == "uranus":
    factor = 0.815
elif planet == "neptune":
    factor = 1.14
else:
    print("Unknown planet. Please enter a valid planet from the list.")
    exit()  # Stop the program

# Step 4: Calculate weight on selected planet
planet_weight = earth_weight * factor

# Step 5: Round and print the result
planet_weight = round(planet_weight, 2)
print("The equivalent weight on", planet.capitalize() + ":", planet_weight)
