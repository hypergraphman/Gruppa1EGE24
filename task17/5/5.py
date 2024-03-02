a = [int(x) for x in open('17.txt')]

b = []
for t1, t2, t3 in zip(a, a[1:], a[2:]):
    t1, t2, t3 = sorted([t1, t2, t3])
    if (t2 - t1) == (t3 - t2) > 0 and len(set([t1 % 10, t2 % 10, t3 % 10])) == 3:
        b.append(t3 - t2)
print(len(b), min(b))

a = [int(i) for i in open('17.txt')]
b = []
for i in range(len(a) - 2):
    q = sorted([a[i], a[i + 1], a[i + 2]])
    if q[1] - q[0] == q[2] - q[1] and q[1] - q[0] > 0 and len(set([q[0] % 10, q[1] % 10, q[2] % 10])) == 3:
        b.append(q[1] - q[0])
print(len(b), min(b))
