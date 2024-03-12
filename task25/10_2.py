def divs(n):
    d = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


def count_even_divs(n):
    count = 0
    for el in divs(n):
        if el % 2 == 0:
            count += 1
    return count


t = 6
k = 1
while t:
    if count_even_divs(777555 - k) % 2 != 0:
        t -= 1
        print(k, count_even_divs(777555 - k))
    k += 1
