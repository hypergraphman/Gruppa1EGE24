from itertools import product

print('x y z w')
for x, y, z, w in product((0, 1), repeat=4):
    f = int(((not x and y) <= w) and ((x and y) <= (z or w)))
    if not f:
        print(x, y, z, w)