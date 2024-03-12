def divs(n):
    if n % 2 == 0:
        return 0
    d = {1, n}
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    if sum(d) % 2 != 0:
        return len(d)
    else:
        return 0


k = 5
n = 1500101
while k:
    m = divs(n)
    if 10 < m < 30:
        k -= 1
        print(n, m, sep='*', end='-')
    n += 2

