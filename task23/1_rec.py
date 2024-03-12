def f(s, fin):
    if s > fin:
        return 0
    if s == fin:
        return 1
    return f(s + 1, fin) + f(s * 2, fin) + f(s * 3, fin)


print(f(1, 10) * f(10, 15))