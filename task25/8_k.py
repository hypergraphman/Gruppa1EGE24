def divs_prime(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if len(divs(i)) == 2:
                d.add(i)
            if len(divs(n // i)) == 2:
                d.add(n // i)
    return sorted(d)


def divs(n):
    d = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


k = 0
for n in range(699999, 1, -1):
    E = sum(divs_prime(n))
    if E != 0 and E % 7 == 0 and n % 5 != 0:
        k += 1
        print(n, E, sep='*', end='-')
    if k == 5:
        break
