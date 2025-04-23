"""
Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function!
"""

def subtract_seven(num):
	num = num - 7
	return num

def main():
	num: int = 7
	num = subtract_seven(num)
	print("This should be zero: ", num)

main()