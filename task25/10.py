def f(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                a.add(i)
            if (n // i) % 2 == 0:
                a.add(n // i)
    return len(a)


for k in range(1, 777555):
    if f(777555 - k) % 2 != 0:
        print(k, f(777555 - k))
