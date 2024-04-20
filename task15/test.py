print(bin(100)[2:].rjust(8, '0'))  # 1100100
print(f'{100:0>8b}')
print(oct(89)[2:].rjust(4, '0'))  # 131
print(f'{89:0>4o}')
print(hex(10)[2:].rjust(2, '0'))  # a
print(f'{10:0>2x}')


from string import digits, ascii_lowercase


def n_to_p(n, p):
    t = ''
    a = digits + ascii_lowercase
    # a = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        d = a[n % p]
        # d = str(n % p)
        t = d + t
        n //= p
    return t


print(n_to_p(100, 2))
print(n_to_p(194, 5))
print(n_to_p(255, 16))
print(int('ff', 16))
print(n_to_p(89, 8))