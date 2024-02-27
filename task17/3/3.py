a = [int(x) for x in open('17.txt')]

# Промежуточное вычисление по всем значениям
avg = sum(a[1::2]) / len(a[1::2])

# Бежим по тройкам и выполняем все условия из задачи
b = []
for t1, t2, t3 in zip(a, a[1:], a[2:]):
    if max(t1, t2, t3) % 2 == 0 and (t1 > avg) + (t2 > avg) + (t3 > avg) >= 2:
        b.append(max(t1 - t2, t2 - t1, t1 - t3, t3 - t1, t2 - t3, t3 - t2))

# Ответы
print(len(b), max(b), sep='*')