# Class Variables and Class Methods
"""
Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.
"""

class Bank():
    bank_name = "Meezan Bank"
    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder} \n Bank Name: {self.bank_name}")

account_01 = Bank("Ali")
account_02 = Bank("Hamzah")

account_01.display()
account_02.display()

Bank.change_bank_name("UBL Bank")
account_01.display()
account_02.display()