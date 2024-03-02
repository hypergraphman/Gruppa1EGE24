a = [int(x) for x in open('17.txt')]

mx = -float('inf')
for el in a:
    if el % 1000 == 131 and el > mx:
        mx = el
b = []
for i in range(len(a) - 2):
    t = sorted(a[i:i + 3])
    if ((1000 <= a[i] < 10000) + (1000 <= a[i + 1] < 10000) + (1000 <= a[i + 2] < 10000) == 1
       and sum(t[:-1]) < mx):
        b.append(min(t[2] - t[1], t[2] - t[0], t[1] - t[0]))
        # b.append(t[0] - t[2])
print(len(b), min(b))