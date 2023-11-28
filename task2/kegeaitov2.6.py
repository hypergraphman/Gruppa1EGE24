from itertools import product

print('x y z')
for x, y, z in product((0, 1), repeat=3):
    f = int((x or z) <= (y == x))
    if not f:
        print(x, y, z)