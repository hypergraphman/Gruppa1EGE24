def f(n):
    s1 = f'{n:b}'
    s2 = s1[1:]
    return int(s2, 2)


a = set()
for i in range(131, 3131):
    a.add(i - f(i))
print(len(a))

b = []
for i in range(131, 3131):
    if i - f(i) not in b:
        b.append(i - f(i))
print(len(b))