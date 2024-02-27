a = [int(x) for x in open('17.txt')]

# Промежуточное вычисление по всем значениям
avg = sum(a) / len(a)

# Бежим по парам и выполняем все условия из задачи
b = []
for p1, p2 in zip(a, a[1:]):
    if (p1 + p2) % 100 == 13 and (p1 < avg or p2 < avg):
        b.append(p1 + p2)

# Ответы
print(len(b), min(b))