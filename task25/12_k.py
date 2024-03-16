from fnmatch import fnmatch


def divs(n):
    d = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


def is_prime(n):
    return len(divs(n)) == 2


def prime_divs(n):
    d = []
    for el in divs(n):
        if is_prime(el):
            d.append(el)
    return d


def s_dig(n):
    s = 0
    for el in prime_divs(n):
        s += sum(map(int, str(el)))
    return s


k = 0
for n in range(1699999, 1, -1):
    if fnmatch(str(n), '*131*?') and len(prime_divs(n)) >= 3 and not fnmatch(str(n), '*9*'):
        k += 1
        print(n, s_dig(n), sep='*', end='-')
    if k == 7:
        break
