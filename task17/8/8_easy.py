a = [int(x) for x in open('17.txt')]

s = 0
for el in a:
    if 7 <= abs(el) % 131 <= 11:
        for c in str(abs(el)):
            s += int(c)
b = []
for i in range(len(a) - 2):
    t1, t2, t3 = a[i], a[i + 1], a[i + 2]
    if ((abs(t1) % 10 == 5 or abs(t2) % 10 == 5 or abs(t3) % 10 == 5)
       and (t1 < s) + (t2 < s) + (t3 < s) == 1):
        sum_t = 0
        for el in t1, t2, t3:
            for c in str(abs(el)):
                sum_t += int(c)
        b.append(sum_t)
print(len(b), min(b))