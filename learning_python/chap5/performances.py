from time import time

mx = 5000

t = time()
dmloop = []
for a in range(1, mx):
    for b in range(a, mx):
        dmloop.append(divmod(a, b))

print('for loop: {:.4f} s'.format(time() - t))

t = time()
dmlist = [divmod(a, b) for a in range(1, mx) for b in range(a, mx)]

print('list comprehension: {:.4f} s'.format(time() - t))

t = time()
dmgen = list(divmod(a, b) for a in range(1, mx) for b in range(a, mx))

print('generator expression: {:.4f} s'.format(time() - t))

print(dmloop == dmlist == dmgen, len(dmloop))
