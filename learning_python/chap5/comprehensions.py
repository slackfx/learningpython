squares = [n ** 2 for n in range(10)] # generates a list with the square of the first ten natural numbers

sq1 = list(filter(lambda n: not n % 2, map(lambda n: n ** 2, range(10))))
sq2 = [n ** 2 for n in range(10) if not n % 2] # the same funcking result as above!!!!


# pairs.for.loop
items = 'ABCDE'
pairs = []
for a in range(len(items)):
    for b in range(a, len(items)):
        pairs.append((items[a], items[b]))

print(pairs)

# same result as above
items = 'ABCDE'
pairs = [(items[a], items[b]) for a in range(len(items)) for b in range(a, len(items))]
print(pairs)

print('#' * 100)

# pythagorean.triple
# pythagorean triple is (a**2) + (b**2) = c ** 2

from math import sqrt
#this will generate all possible pairs
mx = 10
legs = [(a, b, sqrt(a ** 2 + b ** 2)) for a in range(1, mx) for b in range(a, mx)]
#this will filter out all non pythagorean triples
legs = list(filter(lambda triple: triple[2].is_integer(), legs))
# this will make the third number of the tuples integer
legs = map(lambda triple: triple[:2] + (int(triple[2]), ), legs)
print(list(legs))


# same result as above
mx = 10
legs = [(a, b, sqrt(a ** 2 + b ** 2)) for a in range(1, mx) for b in range(a, mx)]
legs = [(a, b, int(c)) for a, b, c in legs if c.is_integer()]
print(legs)

print('#' * 100)

# using dict

from string import ascii_lowercase
lettermap = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))
print(lettermap)

# same as above
lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}
print(lettermap)

print('#' * 100)

# set comprehension
word = 'Hello'
letters1 = set(c for c in word)
letters2 = {c for c in word}
print(letters1)
print(letters2)
print('letters1 == letters2: ', letters1 == letters2)
