from itertools import product

a = list(product('01', repeat=9))
count = 0
for i in range(len(a)):
    line = ''.join(a[i])
    if line.count('1') % 3 == 2:
        count += 1
print(count)