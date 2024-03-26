from math import ceil, floor

f = open('26.txt')
n = f.readline()
a = [int(x) for x in f.readlines()]
a.sort()
print(floor(sum(a[len(a) // 3 * 2:]) * 0.67) + sum(a[:len(a) // 3 * 2]))
print(ceil(sum(a[:len(a) // 3]) * 0.67) + sum(a[len(a) // 3:]))
