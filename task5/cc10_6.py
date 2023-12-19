def f(n):
    s = str(n)
    a = [int(p1 + p2) for p1, p2 in zip(s, s[1:])]
    return max(a) + min(a)


for n in range(10, 1000):
    if f(n) == 131:
        print(n)
        break

