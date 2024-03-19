def f(st, k):
    global a
    if k > 5 or st > 50:
        return None
    if k == 5 and 30 <= st <= 50:
        return st

    a.add(f(st + 1, k + 1))
    a.add(f(st + 5, k + 1))
    a.add(f(st * 2, k + 1))


a = set()
f(1, 0)
a = a - {None}
print(a)
print(len(a))