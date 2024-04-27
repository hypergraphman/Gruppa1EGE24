s = open('24.txt').read().strip()
b = []
for w in s.split('FAT'):
    b += w.split('BAD')
k = len(s)
for p1, p2 in zip(b, b[1:]):
    k = min(len(p1) + len(p2), k)
print(k + 9)