# Function to calculate square
def square(prompt):
    return prompt ** 2 

user_prompt = float(input("Enter number: "))
response = square(user_prompt)  
print("Square of the number is:", response)  
