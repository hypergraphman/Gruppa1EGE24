f = open('24.txt')
s = f.readline().strip()
cur_len = 0
max_len = 0
for i in range(0, len(s) - 1, 2):
    if s[i] + s[i + 1] in ['AT', 'AG']:
        cur_len += 1
    else:
        cur_len = 0
    if cur_len > max_len:
        max_len = cur_len
print(max_len)