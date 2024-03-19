def f(st, fn):
    if st > fn or st == 11:
        return 0
    if st == fn:
        return 1
    m = [f(st + 1, fn),
         f(st + 3, fn),
         f(st * 3, fn)]
    return sum(m)


for i in range(12, 1000):
    if f(1, 10) * f(10, i) == 132:
        print(i)