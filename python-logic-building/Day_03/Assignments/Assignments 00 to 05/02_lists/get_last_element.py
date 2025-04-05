"""
Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.
"""

def get_last_element(lst):

    """
    Prints the last element of a provided list.
    """

    print(lst[-1])

def get_last():

    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """

    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
     lst = get_last()  # Storing 2nd function in a variable 
     get_last_element(lst) # Then giving as an arguement of first function 

if __name__ == '__main__':
    main()