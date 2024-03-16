def f(st, fn):
    if st > fn or st in [7, 12, 17]:
        return 0
    if st == fn:
        return 1
    m = [f(st + 1, fn),
         f(st + 4, fn),
         f(st * 3, fn)]
    return sum(m)


print(f(3, 15) * f(15, 30))