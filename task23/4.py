def f(st, fn, h):
    if st > fn:
        return 0
    if st == fn:
        return h[-2] == '2'
    m = [f(st + 1, fn, h + '1'),
         f(st * 2, fn, h + '2'),
         f(st * 3, fn, h + '2')]
    return sum(m)


print(f(1, 28, ''))