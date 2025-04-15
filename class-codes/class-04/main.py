"""
Topics:
-Variables
-Data Types
-Lists
-Tuples
-Dictionaries
-Functions
-Conditions
-Operators
"""

"""
-Positional Arguments-------Parameters se sync hokr chlte hain iske arguements
-Keyword Arguements
"""
#Functions
#rollno is positional arguement 
#after asterisks are keyword arguements
def Login(rollno, *, email, password, dob):
    user_obj = {
        "rollno":rollno,
        "email": email,
        "password":password,
        "dob":dob  
            }
    print(user_obj)

Login("Giaic2223", "abc@gmail.com", "123", "1st-November")

#Keyword_Arguements
Login("Giaic233", email="abc@gmail.com" , password= "123" , dob='1st-November')
Login("Giaic233", password= "123" , dob='1st-November' ,email="abc@gmail.com" )

#Double Asterisks (For unlimited arguements)
def Binance(**kwargs):
    print(kwargs)

Binance(bitcoin = 23434 , eth = 3344 )

def Wallet(**Items):
    print(Items)

Wallet(Money=20000 , Keys = 5 , Tissue_Packet = 1 , Mobile = 1)

class Teacher(str):
    pass

teacher : str = str("Sir Ali")  #-----str is a class and data type too
Sunday_teacher : str = str("Sir Ali")
print(Sunday_teacher)

teacher : Teacher = "Sir Ali"
Sunday_teacher : Teacher = teacher
print(Sunday_teacher)

teacher : int = int("Sir Ali")  #-----int is a class and data type too
Sunday_teacher : int = int("Sir Ali")
print(Sunday_teacher) #-----code will run and data type issue will not come
teacher.is_integer() #data type helps in vscode intellicence too

#Just in time compiler
#pip install mypy .\app.py ------mypy package to check data type

#python is scripting language, it executes line by line and crash on condition
#Control flow is controlled by conditions (if , else)
#Condition can also run through loop iteration

lst : list = [1, 2, 3]
tpl : tuple = (1, 2, 3)

#Python is high level language
#high level language m behind logic python khd manage krti hai
#low level language wala khd manage krta hai
teacher : Teacher = "Sir Ali"
Sunday_teacher : Teacher = teacher
print(teacher)
print(Sunday_teacher)

lst : list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Dynamic data
tpl : tuple = (1, 2, 3) # Static data

#Immutable ---------string , number
#Mutable ----------- list , dictionary

#Pass by reference
#In python , Mutable data types are pass by reference
teacher : Teacher = "Sir Ali" #H13
Sunday_teacher : Teacher = teacher #H14
teacher : Teacher = "Sir Ahmed Raza" #H13
print(teacher) #---------Sir Ahmed Raza
print(Sunday_teacher) #----------Sir Ali Jawwad

lst : list = [1, 2, 3, 4] #hb12
abc : list = [1, 2, 3, 4] #hb12
lst.append(5) #hb12
abc.append(5) #hb12
print(lst)
print(abc)

def add( x : int, y : int)->int:
    return x + y

# result : int = add(2, 3)
# print(result)

if __name__ == "__main__":
    print(add(2, 3))

