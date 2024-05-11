def divs(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                d.add(i)
            if n // i % 2 == 0:
                d.add(n // i)
    return sorted(d)


for n in range(397438, 443520 + 1, 2):
    if len(divs(n)) >= 142:
        print(len(divs(n)), max(divs(n)), sep='\t')