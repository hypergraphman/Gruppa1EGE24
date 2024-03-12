def divs(n):
    d = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and n % 2 == 1:
            d.add(i)
            d.add(n // i)
    if len(d) == 0:
        return 0
    s = sorted(d)
    if sum(d) % 2 == 1:
        return len(d)
    else:
        return 0


print(divs(5 * 3 * 7))
k = 0
for n in range(1500100, 10000000):
    m = divs(n)
    if m > 10 and m < 30:
        k += 1
        print(n, m, sep='*', end='-')
    if k == 5:
        break
