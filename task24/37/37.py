f = open('24.txt')
s = f.readline().strip()
a = [0]
for i in range(1, len(s) - 1):
    if s[i - 1] + s[i] + s[i + 1] == '131':
        a.append(i)
a.append(len(s) - 1)
max_len = 0
for i in range(0, len(a) - 132):
    if a[i + 132] - a[i] + 1 > max_len:
        max_len = a[i + 132] - a[i] + 1
print(max_len)
