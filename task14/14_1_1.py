def n_to_p(n, p):
    t = ''
    a = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        t = a[n % p] + t
        n //= p
    return t


print(n_to_p(8**5 + 4**5 - 16, 2).count('1'))