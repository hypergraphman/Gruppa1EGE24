def f(st, fn, h):
    if st > fn:
        return 0
    if st == fn:
        return 'BB' not in h
    m = [f(st + 1, fn, h + 'A'),
         f(st * 2, fn, h + 'B'),
         f(st * 3, fn, h + 'C')]
    return sum(m)


print(f(1, 15, ''))