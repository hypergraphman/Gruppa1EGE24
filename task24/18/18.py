f = open('24.txt')
s = f.readline().strip()
# print(s)
k = 0
mx = 0
find = {'NLO', 'NOL'}
for j in range(3):
    for i in range(j, len(s), 3):
        if s[i:i + 3] in find:
            k += 1
        else:
            k = 0
        if k > mx:
            mx = k
print(mx)
