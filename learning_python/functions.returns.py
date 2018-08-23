def separator():
    print("#" * 100)

def factorial(n):
    if n in (0, 1):
        return 1
    result = n
    for k in range(2, n):
        result *= k
    return result

f5 = factorial(5)

print(f5)

separator()

from functools import reduce
from operator import mul

def factorial2(n):
    return reduce(mul, range(1, n+1), 1)

print(factorial2(5))

separator()

# Multiple returns with tuples

def moddiv(a, b):
    return a // b, a % b

print(moddiv(20, 7))
