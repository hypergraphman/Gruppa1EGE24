def f(st, k):
    global a
    if k > 7:
        return None
    if k == 7:
        if st > 0:
            return st
        else:
            return None
    a.add(f(st - 5, k + 1))
    a.add(f(st * (-2), k + 1))


a = set()
f(131, 0)
a = a - {None}
print(a)
print(len(a))
