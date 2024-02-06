f = open('24.txt')
s = f.readline().strip()
cur_len = 5
max_len = 5
start_line = False
for c1, c2, c3, c4, c5, c6 in zip(s, s[1:], s[2:], s[3:], s[4:], s[5:]):
    if c1 + c2 + c3 != c4 + c5 + c6:
        start_line = True
    else:
        start_line = False
        cur_len = 5
    if start_line:
        cur_len += 1
        max_len = max(cur_len, max_len)
print(max_len)
