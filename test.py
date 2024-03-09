from itertools import product

t = ['']
for i in range(1, 3):
    t += [''.join(x) for x in product('0123456789', repeat=i)]
for e in t:
    print(e)