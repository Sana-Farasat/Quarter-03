"""
10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd
"""

# Function to get odd and even numbers
def Odd_Numbers(num):
    even_numbers = []
    odd_numbers = []
    
    for i in num:
        if i % 2 != 0:  # Odd check
            odd_numbers.append(i)
        else:  # Even check
            even_numbers.append(i)
    
    # Print the results
    result = f"Even Numbers: {even_numbers}\nOdd Numbers: {odd_numbers}"
    return result

# Function to take numbers from the user
def get_list():
    lst = []
    while True:
        user_input = input("Enter a number or press enter to stop: ")
        
        if user_input == "":  # Stop if user presses enter without input
            break
        
        try:
            lst.append(int(user_input))  # Convert input to integer and add to list
        except ValueError:
            print("Please enter a valid number.")
    
    return lst

# Main function
def main():
    print("Enter numbers one by one.")
    num_list = get_list()  # Get the list of numbers from the user
    result = Odd_Numbers(num_list)  # Get odd and even numbers
    print(result)  # Print the result

# Call the function to start the program
main()
