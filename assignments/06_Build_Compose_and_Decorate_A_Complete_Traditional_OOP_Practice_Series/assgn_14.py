# Aggregation
"""
Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.
"""

# Aggregation vs Composition
"""
Real-Life Analogy:
Aggregation: A university has students. Students can exist outside a university (they may transfer, drop out, etc.).

Composition: A human has a heart. If the human dies, the heart (functionally) dies too.

🔷 Aggregation vs Composition — dono "has-a" relationships hain, lekin unmein ek important difference hota hai:
Feature	              Aggregation	                  Composition
Relationship	      Weak "has-a"	                 Strong "has-a"
Lifetime	Part can exist independently	Part cannot exist independently
Ownership	      No strict ownership             	Strict ownership
Example	      Department has an Employee	        House has a Room
"""

# Employee class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")

# Department class using aggregation
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: Department "has-a" Employee

    def display(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()

# Creating an Employee object (independent)
emp = Employee("Samreen", 101)

# Creating a Department object that aggregates the Employee
dept = Department("Human Resources", emp)

# Display details
dept.display()
