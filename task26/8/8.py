from collections import defaultdict

f = open('26.txt')
n = int(f.readline())
d = defaultdict(list)
for _ in range(n):
    row, cell = map(int, f.readline().split())
    d[row].append(cell)

is_find = False
for row in sorted(d, reverse=True):
    cells = sorted(d[row])
    for c1, c2 in zip(cells, cells[1:]):
        if c2 - c1 - 1 == 2:
            print(row, c1 + 1)
            is_find = True
            break
    if is_find:
        break
