a = [[0 for _ in range(501)] for _ in range(501)]
f = open('26.txt')
n = int(f.readline())
for _ in range(n):
    row, col = map(int, f.readline().split())
    a[row][col] = 1
for row in range(501):
    for col in range(1, 501 - 6):
        if a[row][col] and a[row][col + 6] and sum(a[row][col + 1:col + 6]) == 0:
            max_row = row
            max_col = col + 5
print(max_row, max_col)