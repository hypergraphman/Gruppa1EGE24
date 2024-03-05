a = [int(x) for x in open('17.txt')]

s = 0
k = 0
for el in a:
    if abs(el) % 100 == 19:
        s += el
        k += 1
avg = s / k
b = []
for t in zip(a, a[1:], a[2:], a[3:]):
    if any(abs(x) % 15 == 12 for x in t) and (sum(x < avg for x in t) >= 2):
        b.append(sum(t))

print(len(b), max(b))
