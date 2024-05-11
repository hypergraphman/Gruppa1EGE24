n, *a = map(int, open('26.txt'))
a.sort()
b = [a.pop()]
for el in a[::-1]:
    if b[-1] - el >= 3:
        b.append(el)
print(len(b), b[-1])
