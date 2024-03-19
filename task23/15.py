def f(s, k):
    global a
    if k == 4:
        return s
    a.add(f(s + 1, k + 1))
    a.add(f(s + 3, k + 1))
    a.add(f(s * 3, k + 1))


a = set()
f(1, 0)
a = a - {None}
print(len(a))
print(a)