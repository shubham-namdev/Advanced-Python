""" A generator-function is defined like a normal function, but whenever it needs to generate a value, 
    it does so with the yield keyword rather than return. 
    If the body of a def contains yield, the function automatically becomes a generator function. 
"""

"""Where using range function is not possible or it may take a lot of memory we can use generators"""


def square(n):
    for i in range(1, n+1):
        yield i**2

squares = square(50)

# the values can be accessed through next keyword
print(next(squares))

# values can also be looped
for s in squares:
    print(s)

"""NOTE: Once the value is used or retrieved the pointer will move to next value, it means the values can be accessed only once."""

"""One advantage of using generator is that we can generate infinite sequences"""

def infinite_numbers():
    ans = 1
    while True:
        yield ans
        ans += 1

# we can print unlimited numbers now as per our requirement
numbers = infinite_numbers()

print(next(numbers))

"""NOTE : now looping will cause infinite loop"""
#for x in numbers :
#    print(x)

"""By using decorators we don't waste memory by storing the whole sequence but we can access the sequence as per our need"""