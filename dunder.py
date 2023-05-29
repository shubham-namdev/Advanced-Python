"""Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name.
   Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading.
"""

from typing import Any

class Name :
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
    
    def __repr__(self) -> str: # representation overloading print()
        return f"Name : {self.fname} {self.lname}"

    def __call__(self) -> None: # when to do when object is called
        print(f"You called {self.fname}")
    
    def __add__(self, other :Any) -> str: # + overloading
        return f"You added {other.fname} to {self.fname}"
    
    def __iadd__(self, other) -> Any: # inplace addition overloading (+=)
        self.fname = other.fname
        self.lname = other.lname
        return self
    
    def __eq__(self, other) -> bool: # == overloading
        return self.fname == other.fname and self.lname == other.lname


my_name = Name("Shubham", "Namdev")
your_name = Name("Shubham", "Namdev")

print(my_name == your_name)

print(my_name)
