f = open('24.txt')
line = f.readline().strip()
cul_len = 1
k = 0
for d1, d2 in zip(line, line[1:]):
    if d2 >= d1:
        cul_len += 1
    else:
        if cul_len == 6:
            k += 1
        cul_len = 1
if cul_len == 6:
    k += 1
print(k)