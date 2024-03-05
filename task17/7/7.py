a = [int(x) for x in open('17.txt')]
mx3, mx2, mx1 = sorted(a)[-3:]
big_sum = mx1 + mx2

b = []
c = []
for t in zip(a, a[1:], a[2:], a[3:]):
    q1, q2, q3, q4 = sorted(t)
    if q2 + q3 + q4 > big_sum and q1 < mx3 / 2:
        b.append(sum(t))
        c.append(q1 + q2)
print(len(b), min(b))
