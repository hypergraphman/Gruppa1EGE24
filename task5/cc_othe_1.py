def n_to_p(n, p):
    t = ''
    a = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        t = a[n % p] + t
        n //= p
    return t


def f(n):
    s1 = n_to_p(n, 3)
    s3 = s1 + s1[-1] * 3
    return int(s3, 3)


a = []
for n in range(1, 131):
    if f(n) >= 1000:
        a.append(f(n))
print(min(a))