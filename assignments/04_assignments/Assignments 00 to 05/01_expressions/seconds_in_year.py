# Constants 
seconds_in_minutes = 60
minutes_in_hour = 60
hours_in_day = 24
days_in_year = 365

def main():
    
    # Calculate seconds in a year
    seconds_in_year = seconds_in_minutes * minutes_in_hour * hours_in_day * days_in_year

    # Print out the result
    print(f" \n There are {seconds_in_year} seconds in a year.. \n")

main()