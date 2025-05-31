from abc import ABC , abstractmethod
# abc ----> Abstract Base Class

#___________________Object Oriented Programming (OOP)______________________

"""
Four pillars of OOP:
-Inheritance
-Encapsulation
-Polymorphism
-Abstraction
"""

#__________________________Features__________________________________
"""
Reuseability
Modularity
"""

class Car():
    def __init__(self, color):
        self.color = color

    def display(self):
        print(f"{self.color} Car!")
    
car1 = Car("Black")
car2 = Car("White")
car1.display()
car2.display()

class Model(Car):
    def __init__(self, color, model):
        super().__init__(color)
        self.model = model

    def display(self):
        print(f"{self.model} Car has {self.color} color..")

car = Model("Blue" , "Corolla")
car.display()

# class - blueprint / template ---> Structure / Pattern / Guidance
# __init__ ---> Dendor/Magic function

# Parent / Super / Base
class Person():
    # constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_info(self):
        return f"{self.name}"
    
    @abstractmethod
    def calculate_fine(self):
        pass             # No implementation where it is declared

# Polymorphism happens after inheritance
# Same function shoule be defined
# Implementation could be different
# Method Overriding

# Child / Derived / Subclass
class Librarian(Person):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary

    def get_info(self):
        return {
            "name" : self.name,
            "salary" : self.salary
        }
    
    def calculate_fine(self , days):
        return self.salary - days
    
class Member(Person):
    def __init__(self, name, email, mem_id):
        super().__init__(name, email)
        self.mem_id = mem_id

    def get_info(self):
        return [self.name , self.mem_id]
    
    def calculate_fine(self , days):
        return days * 2
        
librarian = Librarian("Sana" , "abc@gmail.com" , 20000)
print(librarian.name)
print(librarian.email)
print(librarian.salary)
print(librarian.get_info())
print(librarian.calculate_fine(2))

member = Member("Samreen" , "efg@gmail.com" , "mem_001")
print(member.name)
print(member.email)
print(member.mem_id)
print(member.get_info())
print(member.calculate_fine(2))

class Library():
    #constructor
    #                      School Library         Karachi 
    def __init__(self,         name,              location   , ):
        #class attributes / class variables / traditionally parameters
        self.books = []
        self.lib_name = name
        self.lib_location = location
        # Declaring private attribute (prefix double underscore)
        self.__expenses = {'salaryExp':1234 , 'billKe':1000}

    def get_expenses(self):
        return self.__expenses
    
    def set_expenses(self , update_expenses):
        # self.__expenses = {'salaryExp':1234567 , 'billKe':1500 , 'furniture':20000}
        self.__expenses = update_expenses
        return self.__expenses

    # class method
    def add_book(self, new_book):
        return self.books.append(new_book)
    
    def remove_book(self, remove_book):
        return self.books.remove(remove_book)
    
    def get_book(self):
        return self.books
    
    def __str__(self):
        return f"Library Name: {self.lib_name}, Location: {self.lib_location}, Books: {self.books}"
        
# Making an object / creating instance of a class
library1 = Library("School Library", "4th Floor")
print(library1)
print(library1.lib_name)
print(library1.lib_location)
print(library1.get_expenses())
print(library1.set_expenses(30000))

# books = library.add_book("English book")
# print(books)

# self class ko refer krega attributes ka means class m variables ko virtually store krega

class Books():
    def __init__(cls, name, author, availability):
        cls.book_name = name
        #cls.book_author = 
        cls.book_author = "Ali Jawwad"
        cls.availability = availability

    def borrow(cls):
        return cls.availability

# Instance of a class
book1 = Books("Poetry", "Allama Iqbal", "True")
print(book1.book_name)
print(book1.book_author)
print(book1.availability)

book2 = Books("Comedy" , "Umer Sharif" , True)

library2 = Library("College Library" , "Lahore")

print(library2.lib_name)
print(library2.lib_location)

# Adding books to the list (In Library)
print(library2.add_book(book1.book_name))
print(library2.add_book(book2.book_name))

# Getting the list of books (In Library)
print(library2.get_book())        

# Removing the book (In Library)
print(library2.remove_book(book2.book_name))

# Fetching the list again after removing
print(library2.get_book())




    