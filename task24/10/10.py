f = open('24.txt')
line = f.readline()
indexes = []
for i in range(1, len(line) - 1):
    if line[i - 1] < line[i] > line[i + 1]:
        indexes.append(i)
max_len = 0
for i1, i2 in zip(indexes, indexes[1:]):
    if i2 - i1 > max_len:
        max_len = i2 - i1
print(max_len)