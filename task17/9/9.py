def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


def is_prime(n):
    return len(divs(n)) == 2


a = [int(x) for x in open('17.txt')]

# Промежуточное вычисление по всем значениям
mx = max(filter(lambda x: x % 3 == 0 and x % 27 != 0, a))

# Бежим по тройкам и выполняем все условия из задачи
b = []
for t1, t2, t3 in zip(a, a[1:], a[2:]):
    if (is_prime(t1) + is_prime(t2) + is_prime(t3) == 2) + (t1 > mx or t2 > mx or t3 > mx) == 1:
        b.append(is_prime(t1) + is_prime(t2) + is_prime(t3))

# Ответы
print(len(b), sum(b), sep='*')