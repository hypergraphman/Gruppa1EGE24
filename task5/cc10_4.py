def s(n, d):
    return n // d if n % d == 0 else n - 1


def f(n):
    s1 = s(n, 3)
    s2 = s(s1, 5)
    s3 = s(s2, 7)
    return s3


# print(f(131))
k = 0
for i in range(1, 10000):
    if f(i) == 1:
        k += 1
print(k)
