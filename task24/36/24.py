s = open('24.txt').readline().strip().replace('L', 'X').split('X')
mx = 0
for line in s:
    t = line.replace('E', 'A').replace('Y', 'A').replace('U', 'A').replace('I', 'A').replace('O', 'A')
    if t.count('A') >= 10:
        a = [len(x) for x in t.split('A')]
        for i in range(len(a) - 11):
            mx = max(mx, sum(a[i:i + 11]) + 10)
    else:
        mx = max(mx, len(t))
print(mx)
