f = open('26.txt')
n = int(f.readline())
t = [0] * 1441
for _ in range(n):
    s, e = map(int, f.readline().split())
    for i in range(s, e + 1):
        t[i] += 1
mx = max(t)
k = 0
for t1, t2 in zip(t, t[1:]):
    if t1 < t2 == mx:
        k += 1
print(k, mx)