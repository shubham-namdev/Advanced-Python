"""
-> METHOD OVEROADING
In python the traditional method overloading as in C++ and Java is not possible.
That's why we use multipledispatch library to achieve this.

? Method 1:
If we use the traditional way to overload the method then we can only use the last
or latest defined method.

? Method 2:
using multipledispatch library.
"""

from multipledispatch import dispatch

@dispatch(int, int)
def add(a: int, b:int) -> int:
    return a + b

@dispatch(int, int, int)
def add(a: int, b: int, c: int) -> int:
    return a + b + c
    
@dispatch(str, int)
def add(s: int, a: int) -> int:
    return ord(s) + a

print(add(5, 10))  
print(add(15, 10, 20))
print(add("a", 10))

"""
? How
In Backend, Dispatcher creates an object which stores different implementation and on runtime,
it selects the appropriate method as the type and number of parameters passed.
"""