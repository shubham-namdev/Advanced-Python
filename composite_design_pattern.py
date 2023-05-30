"""In this we have multiple classes that inherit from same interface
   ans one of those can consist of many of others.

   Ex. One region can consist many sub-regions and those sub-regions
       can consist many other sub-regions.
    
   Creates a Heirarchy or tree like structure and increases the flexibility.
"""

from abc import ABCMeta, abstractstaticmethod, abstractmethod
 

class IDepartment(metaclass = ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        """Implemented on sub-class"""

    @abstractstaticmethod
    def info():
        """Implemented on sub-class"""


class HeadDepartment(IDepartment): # Parent Department
    def __init__(self, employees) -> None:
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept) -> None:
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def info(self) -> None:
        print("Head Department")
        print(f"Base Employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.info()
        print(f"Total number of employees: {self.employees}")

class Accounts(IDepartment):
    def __init__(self, employees) -> None:
        self.employees = employees
    
    def info(self):
        print(f"Accounts Department: {self.employees}")

class HR(IDepartment):
    def __init__(self, employees) -> None:
        self.employees = employees
    
    def info(self):
        print(f"HR Department: {self.employees}")

d1 = Accounts(50)
d2 = HR(100)
head = HeadDepartment(15)
head.add(d1)
head.add(d2)

head.info()

"""
Head Department
Base Employees: 15
Accounts Department: 50
HR Department: 100
Total number of employees: 165
"""
