from fnmatch import fnmatch
from itertools import product

digits = ['']
for i in range(1, 9 - 3 + 1):
    digits += [''.join(x) for x in product('0123456789', repeat=i)]
for d2 in digits:
    digits_2 = ['']
    for j in range(1, 9 - 3 - len(d2) + 1):
        digits_2 += [''.join(x) for x in product('0123456789', repeat=j)]
    for d1 in digits_2:
        t = f'9{d1}4{d2}0'
        if int(t) % 47 == 0 and all(t[x] > t[x + 1] for x in range(len(t) - 1)):
            print(t, int(t) // 47)