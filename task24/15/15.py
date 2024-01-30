from itertools import product

f = open('24.txt')
s = f.readline().strip()
cur_len = 1
max_len = 0
max_i = 0
t = [''.join(x) for x in product('KEG', repeat=2)]
print(t)
for i in range(1, len(s)):
    if s[i - 1] + s[i] not in t:
        cur_len += 1
    else:
        cur_len = 1
    if cur_len > max_len:
        max_len = cur_len
print(max_len)