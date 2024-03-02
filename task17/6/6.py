a = [int(x) for x in open('17.txt')]

s = 0
k = 0
for el in a:
    if abs(el) % 100 == 19:
        s += el
        k += 1
avg = s / k
b = []
for q1, q2, q3, q4 in zip(a, a[1:], a[2:], a[3:]):
    t = [q1, q2, q3, q4]
    if any(abs(x) % 15 == 11 for x in t) and (sum(x < avg for x in t) >= 2):
        b.append(sum(t))

print(len(b), max(b))
