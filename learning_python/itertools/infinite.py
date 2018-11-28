from itertools import count

for n in count(5, 3): # count starting from 5 adding 3 untill infinite
    if n > 20:
        break
    print(n, end=', ') # instead of newline, comma and space
