""" Encapsulation describes the idea of wrapping data and the methods that work
    on data within one unit.This puts restrictions on accessing variables and
    methods directly and can prevent the accidental modification of data.To
    prevent accidental change, an object's variable can only be changed by an
    object's method.
"""


class Person:
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.__name = name  # double underscore defines variable as private
        self.__age = age
        self.__gender = gender

    @property
    def Name(self) -> str:  # getter function conventionally starts with capital letter; has to be annotated with @property
        return self.__name
    
    @Name.setter
    def Name(self, new_name : str) -> None:  # setter function to set the new name
        self.__name  = new_name

    @staticmethod
    def example_method():  # static method is not related to any specific object or the class that's why self is not passed. 
                           # Static methods can be called without object creation
        print("I am a static method!")
    


Person.example_method()  # directly calling the static method

p1 = Person("Kevin", 30, 'm')

print(p1.Name) # getter function call

p1.Name = "Kevin Nash" # setter function call
print(p1.Name)