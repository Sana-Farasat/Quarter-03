# Function to ask user favourite's animal
def main():
    try:
        # Get input from user
        animal = input("\n What is your favourite animal? \n ")

        # Ensure the input is a string
        if not animal.isalpha():  # Check if the input contains only alphabets
            raise ValueError("Invalid input! Please enter a valid animal name (letters only).")

        print(f"My favourite animal is also {animal}..")

    except ValueError as e:
        print(e)

# Calling function
main()

#-------------------------------------------------------------------------------------------
# Function to ask user favourite's animal using parameter
def main(prompt):
    return f"My favourite animal is also {prompt}.."

user_input = str(input("What is your favourite animal? "))
response = main(user_input)
print(response)