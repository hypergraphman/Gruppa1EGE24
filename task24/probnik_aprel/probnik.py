s = open('24.txt', 'r').read()
for el in 'KLMN':
    s = s.replace(el, '1')
for el in 'AEOU':
    s = s.replace(el, '0')
k = 1
mx = 1
for i in range(len(s) - 1):
    p1, p2 = s[i], s[i + 1]
    if p1 != p2:
        k += 1
    else:
        k = 1
    mx = max(k, mx)
print(mx)