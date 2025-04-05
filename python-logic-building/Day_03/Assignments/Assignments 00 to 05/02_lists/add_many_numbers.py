"""
Write a function that takes a list of numbers and returns the sum of those numbers.
"""

def add_many_numbers(numbers):

    total : int = 0

    for number in numbers:
        total += number

    return total

# First method
result = add_many_numbers([1, 2, 3, 4, 5])  # Passing a list of numbers
print(result)

# Second method
def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # Make a list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)  # Print out the sum above

main()
