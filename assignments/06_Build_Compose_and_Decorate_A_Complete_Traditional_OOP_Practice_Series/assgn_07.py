# Access Modifiers: Public, Private, and Protected
"""
Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens.
"""
# Public (name)
"""➤ A variable accessible from anywhere — inside or outside the class."""

# Protected (_salary)
"""➤ A variable intended to be accessed within the class and its subclasses (by convention)."""

# Private (__ssn)
"""➤ A variable that is name-mangled to restrict access outside the class directly."""

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

    def get__ssn(self): # Private var can be accessed via getter function
        return self.__ssn
    
    def set_salary(self, new_salary): # Updated salary via setter function
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("Salary must be positive in number")

    def display(self):
            print(f"Name: {self.name}") # Public
            print(f"Salary: {self._salary}") # Protected
            print(f"SSN: {self.__ssn}") # Private (only accessible in its own class)

class Manager(Employee):
     def __init__(self, name, salary, ssn, department):
          super().__init__(name, salary, ssn)
          self.department = department

     def show_manager_info(self):
          print(f"Name: {self.name}")
          print(f"Department: {self.department}")
          print(f"Salary: {self._salary}")
          print(f"SSN via getter function: {self.get__ssn()}") # Private (Accessed through getter function in sub-class)

print("-----------------Employee--------------------")
emp = Employee("Ali", 50000, "123-45-6789")
emp.display()

print()

print("------------------Manager----------------------")

manager = Manager("Ali", 80000, "123-45-6780", "General store")
manager.show_manager_info()
manager.set_salary(100000)
print(f"Updated salary {manager._salary}")
print(manager.get__ssn())
print(f"Private ssn via managed: {manager._Employee__ssn}")


