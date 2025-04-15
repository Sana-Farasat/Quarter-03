import requests

print("Hello World !") #To run --> open cli --> python (file name) --> python main.py

name : str = "Ali"
phonenumber : int = 2365789
age : float = 23.78
colors : list = ['red', 'green', 'black']
colors2 : list[str] = ['red', 'green', 'black', 98] 
#Python is dynamic types language
#Python compiler khd se data type ka error nh deta iske lye mypy ata hai
#pip install mypy
#mypy main.py


#Set ------> Sets are unordered and unindexed
#Use case for number guessing game
fruits_name : set = {'apple', 'orange', 'grapes'}
print(fruits_name) #Okay
#print(fruits_name[0]) #Error

#Difference between dictionary and set
#Dictionary is key value pair and set is only values

#Set Methods
#Union , Intersection
#Union merges 2 sets
#Intercetion extracts common values/elements
#Sets does not allow duplicate

#Union
electronic_cust : set = {' ali','ali', 'ahmed', ' nabeel'} # ali will print only one time
garments_cust : set = {'zargham', 'ameen', 'ehsaan','ahmed'} # ahmed will print only one time while ahmed is in both set
merge = electronic_cust.union(garments_cust)
print(merge)

wow_react : set = {'sana', 'areesha', 'komal'}
laugh_react : set = {'sadia', ' sahiba', 'umama'}
heart_react : set = {'haseeb', 'hussain'}
all_react : set = wow_react.union(laugh_react,heart_react)
#Or
all_react2 : set = wow_react | laugh_react | heart_react
print(all_react)

#Intersection
winter_fruits : set = {'banana', 'melon', 'orange'}
summer_fruits : set = {'banana', 'melon', 'mango'}
common_fruits= winter_fruits.intersection(summer_fruits)
print(common_fruits)

if 'orange' in winter_fruits:
    print('oranges')
if 'mango' not in winter_fruits:
    winter_fruits.add('mango')

lunch : set = {'bhindi'}
if "bhindi" in lunch:
    lunch.discard('bhindi') 

my_friends : set = {'Komal', 'Sadia','Areesha', 'Mehak'}
hina_friends : set = {'Komal' , 'Areesha', 'Urooj', 'Hareem'}
mutual_friends : set = my_friends.intersection(hina_friends)
print(mutual_friends)

#Sets
"""
Create a set named fruits containing 'apple' , 'banana' , 'cherry'..
Add 'orange' to the fruits set..
Remove 'banana' from the set..
Check if 'apple' is in the set..
Clear all items from the set..
"""

fruits : set = {'apple' , 'banana' , 'cherry'}

if 'orange' not in fruits:
    fruits.add('orange')

if 'banana' in fruits:
    fruits.discard('banana')

if 'apple' in fruits:
    print('apple')

if 'apple' in fruits:
    fruits.discard('apple')

if 'orange' in fruits:
    fruits.discard('orange')

if 'cherry' in fruits:
    fruits.discard('cherry')

print(fruits)

#Error handling
a = {'apple', ' mango'}
a.append('orange')  #Error
print("Done") # Line by line execution , ye nh chalega uper error ki wja se

try:
    a = {'apple', ' mango'}
    a.append('orange')
    print(a)
except Exception as e:
    print("Error agya bhai saab....")
else:
    print('Yahn tak pohnch gya....')
finally:
    print('Ye tw hoga.....')
# Error any pr except block chalega wrna else chalega or finally hr surat chalega..

#python request ----> search on google

try:
    req = requests.get("https://google.com")
    #req = requests.get("https://jsonplaceholder.typicode.com/posts")
    #print(req.json())
    print(req)
except Exception as e:
    print(e)
    print("Error agya bhai saab....")
else:
    print("Yahn tak pohnch gya.....")
finally:
    print("Done....")
#Status code ----> 200 is ok

#Loop
Class : list = [
    {
        'name': 'Sana',
        'roll_no': 1234
    },
    {
        'name': 'Hina',
        'roll_no': 124
    },
    {
        'name': 'Areej',
        'roll_no': 123
    }
]

for student in Class:
    print(student)

Cart : list = [
    {
        "product": "shoes",
        "price":20
    },
    {
        "product": "bag",
        "price":30
    },
    {
        "product": "suit",
        "price":80
    },
    {
        "product": "purse",
        "price":100
    }
]

total = 0

for item in Cart:
    total += item['price']
print("Total" , total)

total = 0
while True:
    item = input("Please enter price: ")

    if item == 'Done':
        break
    if item.isnumeric():
        total += int(item)
print(total)
    


