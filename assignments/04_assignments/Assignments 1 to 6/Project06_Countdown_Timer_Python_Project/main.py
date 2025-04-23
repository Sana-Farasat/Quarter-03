#Import time module from python standard library
import time

#Function for countdown timer
def Countdown_timer():

    # Initialized variable for seconds
    seconds : int = 0

    while True:
        try:
           user_input = int(input("\nEnter the countdown time in seconds: "))
           if user_input < 0: # User can't enter negative number 
               print("Please enter a positive number !")
               continue
           seconds = user_input # Assign user_input to seconds variable

        except ValueError:
           print("Invalid input.. Please enter a valid input !")
           continue # This keyword will run loop again

        for i in range(seconds, 0, -1):
            print(f"Time left {i} seconds" , end="\r") # end="\r ye keyword loop ko single line m hi update krta rahega.."
            time.sleep(1)
        print("Timer has ended !  ")
        break # This keyword will break loop 

#Call the function
Countdown_timer()



    




