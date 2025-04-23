"""
Fill out the function count_even(lst) which

first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

and then prints the number of even numbers in the list.
"""

"""
even numbers (joh 2 se divide ho jate hain bina remainder ke) 
"""

#Function to show even number list
def count_even(lst):
    count = 0 #Variable to keep counting of even numbers
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(f"Number of even numbers: {count}")

#Main function
def main():
    lst = []
    while True:
        elem = input("Enter an integer or press enter to stop: ")
        if elem == "":
            break
        try:
            number = int(elem)
            lst.append(number)
        except ValueError:
            print("Please enter a valid integer.")

    count_even(lst)

#Call the function
main()

