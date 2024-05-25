f = open('27_A_2.txt')
n = int(f.readline())
s = 0
d1 = []
d2 = []
for _ in range(n):
    p1, p2 = map(int, f.readline().split())
    s += max(p1, p2)
    d = abs(p1 - p2)
    if d % 3 == 1:
        d1.append(d)
    if d % 3 == 2:
        d2.append(d)
d1.sort()
d2.sort()
print(d1[:2])
print(d2[:2])
print(s)