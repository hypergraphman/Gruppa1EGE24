from collections import Counter

f = open('24.txt')
s = f.readline().strip()
a = []
for c1, c2 in zip(s, s[1:]):
    if c1 == 'V':
        a.append(c2)
print(Counter(a))
print(sorted('vrs'))