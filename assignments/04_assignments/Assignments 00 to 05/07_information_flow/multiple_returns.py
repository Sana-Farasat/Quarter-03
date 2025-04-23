"""
There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.

To practice this, imagine we are working on a program where the user needs to enters data to sign up for a website. Fill out the get_user_data() function which:

Asks the user for their first name and stores it in a variable

Asks the user for their last name and stores it in a variable

Asks the user for their email address and stores it in a variable

Returns all three of these pieces of data in the order it was asked

You can return multiple pieces of data by separating each piece with a comma in the return line.

What is your first name?: Jane

What is your last name?: Stanford

What is your email address?: janestanford@stanford.edu

Received the following user data: ('Jane', 'Stanford', 'janestanford@stanford.edu')

(Note. This idea is called tuple packing/unpacking. We "pack" our return values into a single data structure called a tuple. We can then "unpack" these values back into our original values or leave them as a tuple.)
"""

def get_user_info():
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address : str = input("What is your email address?: ")
    
    return first_name, last_name, email_address

def main():
    user_data = get_user_info()
    print("Received the following user data:", user_data)

if __name__ == "__main__":
     main()

"""
Tuple Packing and Unpacking Python..

Tuple Packing:
Jab hum multiple values ko ek single tuple mein rakh dete hain, use packing kehte hain.

Tuple Unpacking:
Jab hum ek tuple se individual values wapas alag-alag variables mein nikaalte hain, use unpacking kehte hain.

# Packing
a = 5
b = 10
packed = (a, b)  # Packing into a tuple
print(packed)    # Output: (5, 10)
Yaha a aur b ko ek tuple (a, b) mein pack kiya gaya.

# Unpacking
x, y = packed
print(x)  # Output: 5
print(y)  # Output: 10
Yaha humne packed tuple ko x aur y mein unpack kiya.

def get_position():
    x = 3
    y = 7
    return x, y  # Tuple packing

# Unpacking the return values
pos_x, pos_y = get_position()
print(pos_x)  # 3
print(pos_y)  # 7
📌 Yahan:

return x, y → tuple pack ho gaya automatically (returns (3, 7))

pos_x, pos_y = get_position() → tuple unpack ho gaya into pos_x = 3 and pos_y = 7
"""