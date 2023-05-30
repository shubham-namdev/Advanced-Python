"""In singleton design pattern we have only a class 
   and that class can only have one single instance
"""
from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):
    @abstractstaticmethod
    def introduce():
        """Interface Method"""


class PersonSingleton(IPerson):
    __instance = None
    
    def __init__(self, name: str, age: int )->None:
        if PersonSingleton.__instance != None:
            raise Exception(f"Singleton cannot be instantiated more than once!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance
    
    @staticmethod
    def introduce():
        print(f"Hello! My name is {PersonSingleton.__instance.name}. I am {PersonSingleton.__instance.age} years old.")

p1 = PersonSingleton("Jack", 21)
p1.introduce()  
#p2 = PersonSingleton("Oggy", 18)  # This line will raise exception
    