# Method Resolution Order (MRO) and Diamond Inheritance
"""
Create four classes:

A with a method show(),

B and C that inherit from A and override show(),

D that inherits from both B and C.

Create an object of D and call show() to observe MRO.
"""

# MRO Def
"""
🔷 MRO (Method Resolution Order):
MRO batata hai ki jab kisi object se method ya attribute call kiya jata hai, to Python kis class se pehle dhoondhna shuru karta hai.

➡️ Jab multiple inheritance hoti hai (ek class ko do ya zyada classes inherit karti hain), tab Python ek specific order follow karta hai jisko MRO kehte hain.
"""

# Diamond Inheritance Def:
"""
Diamond Inheritance tab hota hai jab ek class do classes se inherit karti hai, jo dono ek hi base class se inherit karti hain.
"""
class A:
    def show(self):
        print("A.show()")

class B(A):
    def show(self):
        print("B.show()")

class C(A):
    def show(self):
        print("C.show()")

class D(B, C):  # Diamond inheritance
    pass

# Create object of class D
d = D()
d.show()

# Print the Method Resolution Order
print(D.__mro__)
