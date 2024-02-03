f = open('24_21.txt')
s = f.readline().strip()
cur_len = 0
max_len = 0
template = 'LISA'
for _ in range(len(template)):
    template = template[1:] + template[0]
    for c in s:
        if c == template[cur_len % len(template)]:
            cur_len += 1
        elif c == template[0]:
            cur_len = 1
        else:
            cur_len = 0
        max_len = max(max_len, cur_len)

print(max_len)