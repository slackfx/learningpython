from itertools import compress

data = range(10) # 0 -> 9
even_selector = [1, 0] * 10 # repeat 10 times the list
odd_selector = [0, 1] * 10

even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))

print(even_selector)
print(odd_selector)
print(list(data)) # without the list() will print 'range(10)' instead of the list representation
print(even_numbers)
print(odd_numbers)
