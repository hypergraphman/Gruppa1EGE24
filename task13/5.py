from itertools import product

a = list(product('01', repeat=12))
count = 0
for i in range(len(a)):
    line = ''.join(a[i])
    if line.count('1') >= 4:
        count += 1
print(count)


# print(len(list(filter(lambda line: line.count('1') >= 4, [''.join(x) for x in product('01', repeat=12)]))))