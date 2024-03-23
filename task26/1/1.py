f = open('test.txt')
s, n = map(int, f.readline().split())
a = [int(line) for line in f]
a.sort()
i = 0
while s - a[i] >= 0:
    s -= a[i]
    i += 1
print(i)
s += a[i - 1]
# print(s)
mx = 0
for el in a:
    if el > mx and el <= s:
        mx = el
print(mx)