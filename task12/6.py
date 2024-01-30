k = 0
for n in range(1, 1000):
    line = '0' + '2' * n
    while '02' in line or '2222' in line or '4422' in line:
        if '02' in line:
            line = line.replace('02', '44', 1)
        if '4422' in line:
            line = line.replace('4422', '20', 1)
        if '2222' in line:
            line = line.replace('2222', '0', 1)
    if sum(map(int, line)) == 100:
        k += 1
print(k)