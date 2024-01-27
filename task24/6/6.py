f = open('24.txt')
line = f.readline().strip()
cur_len = 1
max_len = 1
last_index = 0
for i in range(1, len(line)):
    if line[i - 1] != line[i]:
        cur_len += 1
        if cur_len >= max_len:
            max_len = cur_len
            last_index = i
    else:
        cur_len = 1
print(line[last_index - max_len + 1:last_index + 1])

# YXYZXZYZXYZXYZYXYXYXZYZXYXYZXYX
# XYZYXZYZXYZXYZYXYXYXZYZXYXYZXYX