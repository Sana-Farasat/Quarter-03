"""
There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

How many (apple) do you want?: 0

How many (banana) do you want?: 1

How many (mango) do you want?: 3

Your total is $99.5
"""

#Main function
def main():
    #Storing fruits with their prices in a dictionary
    fruits_dict = {
        'apple': 10,
        'mango': 20,
        'banana': 30,
        'orange': 40,
        'cherry': 50
    }

    total_cost = 0
    """
    This for loop goes through every fruit in the dictionary.

    The loop will pick one fruit at a time, and the name of the fruit is stored in the variable fruits.
    """
    for fruits in fruits_dict:
        price = fruits_dict[fruits]
        amount_bought = int(input("How many (" + fruits + ") do you want to buy? "))
        total_cost += (price * amount_bought)

    
    print("Your total is $" + str(total_cost))

main()

