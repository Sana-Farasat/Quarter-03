"""
There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!

We've provided you with the ADULT_AGE variable which has the age a person is legally classified as an adult (in the United States). Fill out the is_adult(age) function, which returns True if the function takes an age that is greater than or equal to ADULT_AGE. If the function takes an age less than ADULT_AGE, return False instead.

(Entered age is an adult age)

How old is this person?: 35

True

(Entered age is not an adult age)

How old is this person?: 7

False
"""

ADULT_AGE : int = 18 # U.S. age

def Age(age):

    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    user_age = int(input("Enter your age: ")) 
    result = Age(user_age)
    print(result)

main()