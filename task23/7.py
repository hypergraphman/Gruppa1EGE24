def f(st, fn):
    if st < fn:
        return 0
    if st == fn:
        return 1
    m = [f(st - 1, fn)]
    if st % 2 == 0:
         m.append(f(st // 2, fn))
    if st % 3 == 0:
         m.append(f(st // 3, fn))
    return sum(m)


print(f(30, 1))