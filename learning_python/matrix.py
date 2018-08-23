a = [
        [1, 2],
        [3, 4]
    ]
b = [
        [5, 1],
        [2, 1]
    ]
c = [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)] for r in a]
print(c)

aux = 0
lin = 0
col = 0

m = [[0, 0], [0, 0]]
for r in a:
    for c in zip(*b):
        for i, j in zip(r, c):
            aux += i * j
        m[lin][col] = aux
        col += 1
        aux = 0
    lin += 1
    col = 0
print(m)
