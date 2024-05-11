from itertools import product

words = [''.join(word) for word in product('ВОЗДУХ', repeat=5)]

c = 0
for el in words:
    t = el.replace('О', '0').replace('У', '0').replace('В', '1').replace('Х', '1')
    if t.count('0') == 1 and '01' not in t and '10' not in t:
        c += 1
print(c)