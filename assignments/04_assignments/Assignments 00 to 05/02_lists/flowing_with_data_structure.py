"""
In the information flow lesson, we discussed using a variable storing a number as an example of scope. We saw that changes we made to the number inside a function did not stay unless we returned it. This is true for what we call immutable data types which include things like numbers and strings.

However, there are also mutable data types where changes stay even if we don't return anything. Some examples of mutable data types are lists and dictionaries. This means that you should be mindful when modifying lists and dictionaries within helper functions since their changes stay whether or not you return them.

To see this in action, fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list. Don't return anything and see what happens! Compare this process to the x = change(x) example and note the differences.

The concept of immutable/mutable data types is called mutability.
"""

# Storing user prompt
prompt : str = str('Enter a message to copy: ')

# Declared list and left it empty
lst : list = []

# Function to add message in the list 
def add_three_copies(lst : list , data):
    for i in range(3):
        lst.append(data)

# Main function
def main():
    message : str = input(prompt)
    lst : list = []
    print("List Before: ", lst)
    add_three_copies(lst , message)
    print("List After: ", lst)

# Call the function
main()