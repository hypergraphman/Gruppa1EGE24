s = open('24.txt', 'r').read().strip()
for el in 'CDF':
    s = s.replace(el, '1')
for el in 'AO':
    s = s.replace(el, '0')
a = s.split('10')
mx = 0
for t in zip(a, a[1:], a[2:], a[3:], a[4:], a[5:]):
    mx = max(sum(map(len, t)), mx)
print(mx + 10)
