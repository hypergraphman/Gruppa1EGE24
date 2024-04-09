a = []
f = open('26.txt')
n = int(f.readline())
for _ in range(n):
    row, col = map(int, f.readline().split())
    a.append((row, col))
a.sort()
for (row1, col1), (row2, col2) in zip(a, a[1:]):
    if row1 == row2 and col2 - col1 == 6:
        max_row = row1
        max_col = col2 - 1
print(max_row, max_col)
