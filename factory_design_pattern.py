"""Factory design pattern is one of the many object oriented design patterns.
   The goal of a design pattern is usually to increase the modularity, to increase
   the separation of concerns. Meaning the individual pieces of code minf their
   own business and be very good at it.

   Factory design pattern is very useful when we want to decide duriing runtime what 
   particular instance we wanna create.
"""
"""Creating an abstract class Person"""

from abc import ABCMeta, abstractstaticmethod

class Iperson(metaclass = ABCMeta):  # by conention interface names start with 'I'
    @abstractstaticmethod            # as there is no interface keyword in python
    def introduce():
        """Interface Method ;  has to be implemented by subclasses"""


class Student(Iperson):
    def __init__(self) -> None:
        self.name = "Common Student"
    
    def introduce(self):
        print("Hello I am a student!")

class Teacher(Iperson):
    def __init__(self) -> None:
        self.name = "Common Teacher"

    def introduce(self):
        print("Hello I am a teacher!")

#s1 = Student()
#s1.introduce()
#
#t1 = Teacher()
#t1.introduce()

"""Now as we have created the Classes let's see how we will decide the instance
   during runtime.

   In Factory Design Pattern we have a factory class that builds objects.
"""

class PersonFactory:
    @staticmethod
    def build_person(person_type: str):
        if person_type == 'Student':
            return Student()
        if person_type == "Teacher":
            return Teacher()
        """If person_type is invalid"""        
        raise Exception(f"Undefined person_type : {person_type}")

if __name__ == "__main__":
    choice = input("Type of person: ")
    person = PersonFactory.build_person(choice)
    person.introduce()

