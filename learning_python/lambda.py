# without lambda

def is_multiple_of_five(n):
    return not n % 5

def get_multiples_of_five(n):
    return list(filter(is_multiple_of_five, range(n)))

print(get_multiples_of_five(50))

# Using lambda

def get_multiples_of_five2(n):
    return list(filter(lambda k: not k % 5, range(n)))


print(get_multiples_of_five(50))

# adder

def adder(a, b):
    return a + b

# is equivalent to 

adder_lambda = lambda a, b: a + b

# to uppercase
def to_uppercase(s):
    return s.upper()

# is equivalent to 
to_upper_lambda = lambda s: s.upper()
