def f(st, fn, k):
    if st > fn or k > 7:
        return 0
    if st == fn and k <= 7:
        return 1
    m = [f(st + 1, fn, k + (st + 1 + 1) % 2),
         f(st * 2, fn, k + (st * 2 + 1) % 2),
         f(st * 3, fn, k + (st * 3 + 1) % 2)]
    return sum(m)


print(f(1, 131, (1 + 1) % 2))