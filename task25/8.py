def divs(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if divs(i) == 0:
                d.add(i)
            if divs(n // i) == 0:
                d.add(n // i)

    if len(d) == 0:
        return 0
    s = sorted(d)
    return int(sum(d))


print(divs(70))
k = 0
for n in range(700000, 1000, -1):
    m = divs(n)
    if n % 5 != 0 and m != 0 and m % 7 == 0:
        k += 1
        print(n, m, sep='*', end='-')
    if k == 5:
        break
