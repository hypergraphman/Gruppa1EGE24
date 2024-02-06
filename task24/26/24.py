f = open('24.txt')
min_len = float('inf')
cur_len = 0
start_line = False
for c in f.readline().strip():
    if c == 'A':
        start_line = True
        cur_len = 0
    if start_line:
        cur_len += 1
    if c == 'Z' and cur_len > 2:
        start_line = False
        min_len = min(min_len, cur_len)
print(min_len)
