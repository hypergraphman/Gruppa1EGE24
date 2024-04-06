with open('26.txt') as f:
    n, m, *a = map(int, f.read().split())
a.sort()
first = []
second = []
for x in a:
    if 170 <= x <= 180:
        first.append(x)
    else:
        second.append(x)
m -= sum(first)

goods_in_truck = []
while second[0] <= m:
    goods_in_truck.append(second.pop(0))
    m -= goods_in_truck[-1]
print('ответ 1:', len(first) + len(goods_in_truck))


i = len(second) - 1
j = len(goods_in_truck) - 1
while i >= 0:
    if m + goods_in_truck[j] - second[i] >= 0:
        m = m + goods_in_truck[j] - second[i]
        second.insert(0, goods_in_truck.pop(j))
        goods_in_truck.insert(j, second.pop(i + 1))
        j -= 1
    else:
        i -= 1
print(m)
print('Ответ 2:', sum(first) + sum(goods_in_truck))
