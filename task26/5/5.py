f = open('26.txt')
n, m = map(int, f.readline().split())
data = [int(x) for x in f]
# start = [x for x in data if 170 <= x <= 180]
# dalee = sorted([x for x in data if not (170 <= x <= 180)])
a = []
k = 0
for el in data:
    if 170 <= el <= 180 and m - el >= 0:
        m -= el
        k += 1
    if not (170 <= el <= 180):
        a.append(el)
# print(m, k)
a.sort(reverse=True)
b = []
b.append(a.pop())
while m - b[-1] >= 0:
    k += 1
    m -= b[-1]
    b.append(a.pop())
print(k)

a.append(b.pop())
# b.sort(reverse=True)
i = 0
m += b.pop()
while i < len(a) and m < a[i]:
    i += 1
while i < len(a) and m >= a[i]:
    m -= a[i]
    i += 1
    x = b.pop()
    a.append(x)
    m += x
    while i < len(a) and m < a[i]:
        i += 1
print(m)
print(m - x)
