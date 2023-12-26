from collections import Counter


def n_to_p(n, p):
    t = ''
    a = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        t = a[n % p] + t
        n //= p
    return t


c = Counter(n_to_p(45*400**10 - 8**5*5**8 + 16*20**3 - 33, 20))
k = 0
for key in c:
    if key.isdigit():
        k += c[key]
print(k)