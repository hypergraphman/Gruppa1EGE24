f = open('24.txt')
line = f.readline()
cur_len = 0
max_len = 0
for el in line:
    if el == 'Y':
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 0
print(max_len)