n, v, *a = map(int, open('26.txt').read().split())
s = 0
k = 0
free = []
for el in a:
    if 170 <= el <= 180:
        s += el
        k += 1
    else:
        free.append(el)
truck = []
free.sort()
while sum(truck) + s + free[0] <= v:
    truck.append(free.pop(0))
print('Answer 1:')
print(len(truck) + k)

j = len(free) - 1
i = len(truck) - 1
while j != -1:
    if v - sum(truck) - s + truck[i] >= free[j]:
        truck[i], free[j] = free[j], truck[i]
        free.sort()
        i -= 1
    else:
        j -= 1

print('Answer 2:')
print(sum(truck) + s)
