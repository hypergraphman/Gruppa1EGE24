f = open('24.txt')
s = f.readline()
a = s.split('W')
ans = 9000000
ss = 0
for i in range(len(a) - 99):
    ss = 0
    for j in range(i, i + 99):
        ss += len(a[j])
    if ss < ans:
        ans = ss
print(ans + 100)
