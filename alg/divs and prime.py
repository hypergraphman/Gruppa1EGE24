def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


def is_prime(n):
    return len(divs(n)) == 2


for n in range(1, 100):
    if is_prime(103 + n * 7):
        print(n, 103 + n * 7)