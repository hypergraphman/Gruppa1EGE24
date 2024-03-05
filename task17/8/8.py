a = [int(x) for x in open('17.txt')]

s = 0
for el in filter(lambda x: abs(x) % 131 in {7, 8, 9, 10, 11}, a):
    s += sum(map(int, str(abs(el))))

b = []
for t in zip(a, a[1:], a[2:]):
    if any(abs(x) % 10 == 5 for x in t) and sum(x < s for x in t) == 1:
        b.append(sum(sum(map(int, str(abs(el)))) for el in t))
print(len(b), min(b))