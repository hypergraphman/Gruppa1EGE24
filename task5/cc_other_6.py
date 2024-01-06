def st23(a):
    s1 = 0
    s2 = 0
    for el in a:
        if el % 2 == 0:
            s2 += el
        else:
            s1 += el
    if s1 > s2:
        return s1 % 80
    return s2 % 80


def f(n):
    a = []
    while n > 0:
        a.append(n % 80)
        n //= 80
    a = a[::-1]
    a.append(st23(a))
    a.append(st23(a))
    a = a[::-1]
    r = 0
    for i in range(len(a)):
        r += a[i] * 80 ** i
    return r


print(f(83))

for i in range(1, 1000):
    if f(i) > 1000000:
        print(i)
        break