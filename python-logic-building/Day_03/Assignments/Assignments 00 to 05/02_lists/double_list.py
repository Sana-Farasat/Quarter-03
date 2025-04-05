"""
Write a program that doubles each element in a list of numbers. 
"""

def main():
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7]  # Creates a list of numbers

    for i in range(len(numbers)):  # Loop through the indices of the list
        elem_at_index = numbers[i]  # Get the element at index i in the numbers list
        numbers[i] = elem_at_index * 2  # Set the element at index i to be equal to the previous element times 2

    print(numbers)  # This should print the doubled list

if __name__ == '__main__':
    main()