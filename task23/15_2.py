def f(st, fn, h):
    if st > fn or h > 4:
        return 0
    if st == fn and h == 4:
        return 1
    m = [f(st + 1, fn, h + 1),
         f(st + 3, fn, h + 1),
         f(st * 3, fn, h + 1)]
    return sum(m)


count = 0
for a in range(1, 300):
    if f(1, a, 0) > 0:
        count += 1
print(count)