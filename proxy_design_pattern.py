"""Proxy wraps the functionality around the object creation"""

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):
    @abstractstaticmethod
    def introduce():
        """Interface Method - To be implemented by subclasses"""

class Person(IPerson):
    def introduce(self) -> None:
        print("Hello I am a person!")

""" We are going to use a proxy or middle man to instantiate the person object. """

class ProxyPerson(IPerson):
    def __init__(self) -> None:
        self.person = Person()

    def introduce(self):
        print("Hello I am a Proxy Person!")
        self.person.introduce()


p1 = Person()
p1.introduce()

p2 = ProxyPerson()
p2.introduce()


