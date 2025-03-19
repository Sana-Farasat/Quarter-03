from termcolor import colored

print(colored("\n\t\t\t +-+-+Simple Grading System+-+-+\n", "green"))

#Taking inputs from user
obtained_marks= int(input(colored("Enter your obtained marks: ", "yellow")))
total_marks= int(input(colored("Enter your total marks: ", "yellow")))

#Calculating percentage
percentage= obtained_marks/total_marks * 100

# Format the percentage to 2 decimal places
percentage = round(percentage, 2)
 
#Result based on Percentages
if percentage >= 90:
   print(colored(f"percentage: {percentage}%", "red"))
   print(colored("Grade A-One🎓","blue"))
elif percentage >= 80:
   print(colored(f"percentage: {percentage}%", "red"))
   print(colored("Grade A🎓","blue"))
elif percentage >= 70:
   print(colored(f"percentage: {percentage}%", "red"))
   print(colored("Grade B👏","blue"))
elif percentage >= 60:
   print(colored(f"percentage: {percentage}%", "red"))
   print(colored("Grade C👏","blue"))
elif percentage >= 50:
   print(colored(f"percentage: {percentage}%", "red"))
   print(colored("Grade D👎","blue"))
else:
    print(colored(f"percentage: {percentage}%", "red"))
    print(colored("Failed❌","red"))
    print(colored("You need to work hard...","blue", attrs=["bold"]))

   

