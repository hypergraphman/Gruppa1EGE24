a = [int(x) for x in open('17.txt')]

mx1 = 0
mx2 = 0
mx3 = 0
for el in a:
    if el > mx1:
        mx3 = mx2
        mx2 = mx1
        mx1 = el
    elif el > mx2:
        mx3 = mx2
        mx2 = el
    elif el > mx3:
        mx3 = el
# mx3 = sorted(a)[-3] альтернатива

b = []
for p1, p2, p3 in zip(a, a[1:], a[2:]):
    if (p1 % 2 == 0) + (p2 % 2 == 0) + (p3 % 2 == 0) <= 2 and (p1 + p2 + p3) <= mx3:
        b.append(p1 + p2 + p3)
print(len(b), max(b))
