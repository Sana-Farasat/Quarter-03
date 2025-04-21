# List
import requests


months : list = ['January' , ' February' , 'March' , 'April' , 'May' , 'June', 'July']
print(months)

# Slicing
# Starting point is inclusive ,  Ending point is exclusive/excluded
print(months[0:3])  # ['January' , ' February' , 'March']

print(months[3:6])  # ['April' , 'May' , 'June']
                    # If 6 element exist nh krta list m tw error nh dega phr bh
#print(months[3:])  # Future m jtni values add hngi sb print krega because of missing ending point

# Negative indexing
print(months[-3 , -1]) # Ending point is also exclusive in negative indexing
# If last element print krna ho tw ending point nh dengy 
print(months[0]) = 'December'

# List methods:
# Append
# Pop
# Insert
# Remove
# Slice
# Clear

# Tuples / Immutable Version of list
numbers : tuple[int] = (12, 33, 67, -55, 32, 89 )
print(numbers[0])
print(numbers[0:3])  # Slicing
print(numbers[-4 , -1])
# print(numbers[0]) = 100  # Error because tuples are immutable

# Tuples:
# max
# min

teachers : tuple[str] = ("Ali Jawwad" , "Abdul Haseeb" , "Ali Alhemd")
print(type(teachers))
print(teachers)

# Conversion of tuple to list
tuple_to_list = list(teachers)
print(type(tuple_to_list))
print(tuple_to_list)
print(tuple_to_list.append("Ameen Alam"))

# Conversion of list to tuple  
list_to_tuple = tuple(tuple_to_list)
print(type(list_to_tuple))
print(list_to_tuple)

#Dictionary (Structured Data)
user_info ={
    "student" : "Sana",
    "roll_no" : 12345,
    "courses" : ['Docker' , 'Fast Api' , 'Open Ai Agents'],
    "assignments" : {
        "assgnOne" : "Completed",
        "assgnTwo" : "Inprogress"
    }
}

print(user_info)
print(user_info["courses"][2])  # Access of List (Indexing)
print(user_info["assignments"]["assgnTwo"]) # Access of Dictionary (Key)

# Loops through Dictionary
# For Loop
for abcd in user_info.values():
    print(abcd)

for hello , world in user_info.items():
    print(hello , world)  # hello = keys , world = values

for i in range(1, 9):
    print(i)

#pip install requests ---> package name
#Virtual env active nh hoga tw module not found ka error dega requests module k lye
#If Virtual env active hoga tw wo khdi catch krlega module

#try except is for asynchronous task
try:
    url = requests.get("https://jsonplaceholder.typicode.com/posts")
    res = url.json()
    print(res)

except Exception as e:  # Exception Handling (Exception = Error)
    print("Error message here" , e)

finally:
    print("Request Ended..")
 
# Chatgpt prompt:
# You are a python expert .. Explain this code in simplest words ..







