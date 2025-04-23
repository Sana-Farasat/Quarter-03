import random

"""
30% chance that the counting will stop early (when done() returns True)
It's give a  value between 0 and 1
"""
DONE_LIKELIHOOD = 0.3  # 30% chance of stopping early

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # This stops the function and exits the loop
        print(curr_num)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
