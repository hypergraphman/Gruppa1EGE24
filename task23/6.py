def f(st, fn):
    if st > fn:
        return 0
    if st == fn:
        return 1
    m = [f(st + 1, fn),
         f(st * 3, fn),
         f((st // 10 + 1) * 10, fn)]
    return sum(m)


print(f(1, 10) * f(10, 20) * f(20, 60))