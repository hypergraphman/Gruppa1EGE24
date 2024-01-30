from collections import Counter

f = open('24.txt')
s = f.readline().strip()
a = [0] * 256
for c1, c2 in zip(s, s[1:]):
    if c1 == 'V':
        a[ord(c2)] += 1

mx = max(a)
for i in range(len(a)):
    if a[i] == mx:
        print(chr(i), mx, sep='')
