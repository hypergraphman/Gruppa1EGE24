from itertools import product

print('x y z w')
for x, y, z, w in product((0, 1), repeat=4):
    f1 = int((x == y) and (w <= z))
    f2 = int((x <= y) <= (w == z))
    print(x, y, z, w, f1, f2)