# Storing height
Minimum_Height :int = 50

# Function for ride
def main(prompt):
    
    if prompt >= 50:
       return "You are tall enough to ride! "
    else:
       return "You're not tall enough to ride, but maybe next year!"

user_input = float(input("Please enter your height (in cm): "))
response = main(user_input)
print(response)
