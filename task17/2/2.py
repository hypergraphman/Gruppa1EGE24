a = [int(x) for x in open('17.txt')]

# Промежуточное вычисление по всем значениям
# mn = float('inf')
# for el in a:
#     if abs(el) % 10 == 7 and el < mn:
#         mn = el
mn = min(filter(lambda x: abs(x) % 10 == 7, a))


# Бежим по парам и выполняем все условия из задачи
b = []
for p1, p2 in zip(a, a[1:]):
    if (p1 + p2) % 4 == 0 and (p1 < mn < p2 or p2 < mn < p1):
        b.append(p1 + p2)

# Ответы
print(len(b), max(b), sep='*')