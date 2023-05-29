""" Decorators allow us to wrap another function in order to extend the 
    behaviour of the wrapped function, without permanently modifying it.
"""
import time

def timer(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = function(*args, **kwargs)
        end = time.time()
        print(f"{function.__name__} took {end-start:4f} seconds to execute!")
        return value
    return wrapper




@timer
def multiply(x : int, y : int) -> int:
    ans = 1
    for i in range(1, x+y):
        ans *= i
    return ans
multiply(x = 50000, y = 10000)


"""This timer decorator function can be used to time any function with any number of parameters"""