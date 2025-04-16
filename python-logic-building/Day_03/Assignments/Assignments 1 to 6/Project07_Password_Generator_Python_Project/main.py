import string #Bht sary alphabets digits deta hai
import random #Random numbers k lye

def Generate_password(name ,digit):
    name = name #First 3 letters of your name will be added in generated password
    characters : str = name[:3] + string.ascii_letters + string.digits + '!@#$%^&*-_'
    return name[:3] + "".join(random.choice(characters) for i in range(digit))

    """
    random.choice(characters) selects a random character from the characters string.
    The generator expression (random.choice(characters) for i in range(digit)) repeats this process digit times.
    ''.join(...) concatenates these characters into a single string.
    """
def main():

    user_input = str(input("Enter your name: "))
    user_input2 = int(input("Enter password length to generate password: "))
    
    if user_input2 < 8:
        print("Password length should be atleast 8 characters..")
    else:
        generate_password = Generate_password(user_input , user_input)
        print(f"Generated password: {generate_password}")

main()

"""
In Python, the join() method is used to concatenate elements of an iterable (like a list or tuple) into a single string, inserting a specified separator between each element. When you use an empty string ("") as the separator, it effectively concatenates the elements without any additional characters between them.

''.join(['a', 'b', 'c']) Output: abc

when generating a password, we concatenated randomly chosen characters without any separator. Using ''.join() is appropriate here because it joins the characters directly without adding any extra characters between them.
"""

