for n in range(500, 1000 + 1):
    line = '3' * n
    while '111' in line or '3333' in line:
        if '111' in line:
            line = line.replace('111', '33', 1)
        else:
            line = line.replace('333', '1', 1)
    print(n, line)