f = open('24.txt')
line = f.readline().strip()
k = 0
for c1, c2, c3, c4 in zip(line, line[1:], line[2:], line[3:]):
    if len({c1, c2, c3, c4}) == 4:
        k += 1
print(k)