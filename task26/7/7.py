f = open('26.txt')
k, s = map(int, f.readline().split())
a = []
for _ in range(k):
    let, cost, n = f.readline().split()
    cost, n = int(cost), int(n)
    if let == 'Z':
        s -= cost * n
    else:
        a.append((cost, n))
print(s)
a.sort()
print(a)
i = 0
count = 0
while a[i][0] * a[i][1] < s:
    s -= a[i][0] * a[i][1]
    count += a[i][1]
    i += 1
print(count + s // a[i][0], s % a[i][0])