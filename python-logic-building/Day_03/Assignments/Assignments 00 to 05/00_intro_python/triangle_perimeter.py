# Function for calculating triangle
def triangle(side1, side2, side3):
    print("The perimeter of the triangle is " + str(side1 + side2 + side3))

prompt_01 :float = float(input(" \n What is the length of side 1? ")) 
prompt_02 :float = float(input("What is the length of side 2? ")) 
prompt_03 :float = float(input("What is the length of side 3? "))    

perimeter = triangle(prompt_01,prompt_02, prompt_03)
print(perimeter)