f = open('27_B.txt')
n = int(f.readline())
s = 0
min_d = float('inf')
for _ in range(n):
    p1, p2 = map(int, f.readline().split())
    s += min(p1, p2)
    d = abs(p1 - p2)
    if d % 13 != 0 and d < min_d:
        min_d = d
if s % 13 == 0:
    s += min_d
print(s)