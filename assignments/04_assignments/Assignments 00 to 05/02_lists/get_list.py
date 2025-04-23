"""
Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.
"""

def get_list(lst):

    """
    Print the list...
    """

    print(lst)

def elements():

    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """

    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")

    while elem != "":
        lst.append(elem)
        elem: str = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
     lst = elements()  # Storing 2nd function in a variable 
     get_list(lst) # Then giving as an arguement of first function

if __name__ == '__main__':
    main()


