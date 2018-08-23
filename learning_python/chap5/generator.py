def s():
    print('#' * 100)

def get_squares(n):
    return [x ** 2 for x in range(n)]

print(get_squares(10))

def get_squares_gen(n):
    for x in range(n):
        yield x ** 2 # we yield, we don't return

print(list(get_squares_gen(10)))

squares = get_squares_gen(4)
print(squares)
print(next(squares))
print(squares.__next__())
print(next(squares))
print(squares.__next__())
# print(next(squares)) # error

s()

# gen.yield.return

def geometric_progression(a, q):
    k = 0
    while True:
        result = a * q ** k
        if result <= 100000:
            yield result
        else:
            return
        k += 1

for n in geometric_progression(2, 5):
    print(n)

s()

# gen.send
def counter(start=0):
    n = start
    while True:
        result = yield n
        print(type(result), result)
        if result == 'Q':
            break
        n += 1

#c = counter()
#print(next(c))
#print(c.send('Wow!'))
#print(next(c))
#print(c.send('Q'))

s()

# yield from expression

def print_squares(start, end):
    for n in range(start, end):
        yield n ** 2

for n in print_squares(2, 5):
    print(n)

# same as above
def print_squared2(start, end):
    yield from (n ** 2 for n in range(start, end))

for n in print_squares(2, 5):
    print(n)

s()

# generator expressions
cubes = [k ** 3 for k in range(10)] # regular list
print(type(cubes), cubes)

cubes_gen = (k ** 3 for k in range(10))
print(type(cubes_gen), cubes_gen)
print(list(cubes_gen))
print(list(cubes_gen)) # will be empty

s()

# gen.map

def adder(*n):
    return sum(n)

s1 = sum(map(lambda n: adder(*n), zip(range(100), range(1, 101))))
s2 = sum(adder(*n) for n in zip(range(100), range(1, 101)))
print(s1)
print(s2)

s()

# gen.map

cubes = [x**3 for x in range(10)]
odd_cubes1 = filter(lambda cube: cube % 2, cubes)
odd_cubes2 = (cube for cube in cubes if cube % 2)

print(list(odd_cubes1))
print(list(odd_cubes2))

s()

# gen.map.filter

N = 20
cubes1 = map(
        lambda n: (n, n**3), 
        filter(lambda n: n % 3 == 0 or n % 5 == 0, range(N))
)

cubes2 = ((n, n**3) for n in range(N) if n % 3 == 0 or n % 5 == 0)

print(list(cubes1))
print(list(cubes2))

s()

# sum.example

#s1 = sum([n**2 for n in range(10**6)]) # Comprehension
#s2 = sum((n**2 for n in range(10**6))) # Generator
#s3 = sum(n**2 for n in range(10**6))   # Generator too, the braces are optional

#print(s1)
#print(s2)
#print(s3)

# sum.example.2

#s = sum([n**2 for n in range(10**8)]) # takes forever to run
#s = sum(n**2 for n in range(10**8)) # faster than the above
#print(s)
