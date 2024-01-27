f = open('24.txt')
line = f.readline().strip()
cur_len = 1
max_len = 1
for c1, c2 in zip(line, line[1:]):
    if c1 == c2:
        cur_len += 1
        max_len = max(cur_len, max_len)
    else:
        cur_len = 1
print(max_len)