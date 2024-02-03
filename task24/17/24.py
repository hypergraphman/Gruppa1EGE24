f = open('24.txt')
s = f.readline().strip().replace('L', 'P').replace('N', 'P').replace('I', 'O').replace('A', 'O')
# print(s)
k = 0
mx = 0
for j in range(2):
    for i in range(j, len(s), 2):
        if s[i:i + 2] == 'PO':
            k += 1
        else:
            k = 0
        if k > mx:
            mx = k
print(mx)
