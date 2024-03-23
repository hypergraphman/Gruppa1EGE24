from collections import defaultdict

f = open('26.txt')
p, n = map(int, f.readline().split())
d = defaultdict(list)
for line in f:
    id, mark = map(int, line.split())
    d[id].append(mark * 100)
# print(d)
r = defaultdict(tuple)
for id in d:
    d[id].sort()
    x = int(p * len(d[id]) / 100)
    if x > 0:
        a = d[id][x:-x]
    else:
        a = d[id]
    # print(a)
    avg = sum(a) // len(a)
    med = sum(a[len(a) // 2 - 1:len(a) // 2 + 1]) // 2 if len(a) % 2 == 0 else a[len(a) // 2]
    r[id] = (avg, abs(avg - med))
print(r)

mn = float('inf')
mx_id = -1000
mx_d = 0
for id in r:
    if r[id][0] < mn:
        mn = r[id][0]
    if r[id][1] >= mx_d:
        mx_d = r[id][1]
        if id > mx_id:
            mx_id = id
print(mn, mx_id)