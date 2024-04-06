from math import ceil

# f = open('test.txt.txt')
f = open('26.txt')
f.readline()
a = [int(x) for x in f.readlines()]
s = 0
b = []
for i in range(len(a)):
    if a[i] <= 500:
        s += a[i]
    else:
        b.append(a[i])
b.sort()
for i in range(len(b) // 2):
    s += b[i] * 0.8
    ans = b[i]
for i in range(len(b) // 2, len(b)):
    s += b[i]

print(ceil(s), ans)
