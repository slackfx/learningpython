from lib.module1.sum import sum

def sumlist(*a):
    c = 0
    for num in a:
        c += sum(c, num)
    return c
