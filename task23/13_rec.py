def f(s, fn, k):
    if s > fn or k > 7:
        return 0
    if s == fn:
        return 1
    m = [f(s + 2, fn, k + 1),
         f(s + 3, fn, k + 1),
         f(s * 2, fn, k + 1)]
    return sum(m)


print(f(1, 130, 0))