def n_to_p(n, p):
    t = ''
    a = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        t = a[n % p] + t
        n //= p
    return t


print(len(set(n_to_p(4 * 81**5 + 3**12 - 37, 9))))
print(sum(map(int, n_to_p(4 * 81**5 + 3**12 - 37, 9))))