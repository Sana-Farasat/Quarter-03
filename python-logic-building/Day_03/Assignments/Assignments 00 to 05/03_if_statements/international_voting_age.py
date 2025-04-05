# Storing countries voting age
Peturksbouipo_age :int = 16
Stanlau_age :int = 25
Mayengua_age :int = 48

# Function for voting age on condition basis
def Voting_Age():
    
    prompt = int(input("How old are you? "))

    if prompt >= Peturksbouipo_age:
        print("You can vote in Peturksbouipo where the voting age is " + str(Peturksbouipo_age) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(Peturksbouipo_age) + ".")

    if prompt >= Stanlau_age:
        print("You can vote in Stanlau where the voting age is " + str(Stanlau_age) + ".")
    else:
        print("You cannot vote in Stanlau where the voting age is " + str(Stanlau_age) + ".")

    if prompt >= Mayengua_age:
        print("You can vote in Mayengua where the voting age is " + str(Mayengua_age) + ".")
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(Mayengua_age) + ".")

# Calling function
Voting_Age()