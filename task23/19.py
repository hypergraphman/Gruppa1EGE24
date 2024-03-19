def f(st, fn, k):
    if st > fn or k > 6:
        return 0
    if st == fn and 1 <= k <= 6:
        return 1
    m = [f(st + 1, fn, k + 1),
         f(st * 2, fn, k + 1),
         f(st ** 2, fn, k + 1)]
    return sum(m)


count = 0
for x in range(1, 131):
    if f(x, 131, 0) > 0:
        count += 1
print(count)