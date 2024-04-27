f = open('26.txt')
cells = [0] * (int(f.readline()) + 1)
n = int(f.readline())
p = []
for _ in range(n):
    p.append(tuple(map(int, f.readline().split())))
p.sort()

k = 0
last = 0
for st, fin in p:
    for i in range(1, len(cells)):
        if cells[i] < st:
            k += 1
            last = i
            cells[i] = fin
            break
print(k, last)