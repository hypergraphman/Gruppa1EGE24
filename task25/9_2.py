def divs(n):
    d = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


def divs_c(n):
    d = n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d *= i
    return d


k = 0
for n in range(1500101, 10 ** 10, 1):
    f = divs(n)
    if 10 < len(f) < 30 and sum(f) % 2 != 0 and divs_c(n) % 2 != 0:
        k += 1
        print(n, len(f), sep='*', end='-')
    if k == 5:
        break
