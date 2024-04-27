f = open('24.txt')
s = f.readline()
c = 0
t = 0
ans = 0
for i in range(len(s) - 1):
    if s[i] in 'CDF' and s[i + 1] in 'AO':
        c += 1
        t += 1
        if t > 5:
            ans = max(ans, c)
            t = 1
            c = 2
    else:
        c += 1
    # if t == 5:
    #     ans = max(ans, c)
    #     t = 0
    #     c = 1
print(ans)
