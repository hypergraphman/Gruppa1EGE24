from collections import Counter


def n_to_p(n, p):
    t = ''
    a = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        t = a[n % p] + t
        n //= p
    return t


print(n_to_p(2 * 9 ** 7 - 3 ** 8 - 19, 3).count('2'))
print(Counter(n_to_p(2 * 9 ** 7 - 3 ** 8 - 19, 3)))