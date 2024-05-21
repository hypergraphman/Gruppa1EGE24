f = open('26.txt')
n = f.readline()
data = []
for i, line in enumerate(f, start=1):
    g, p = map(int, line.split())
    data.append((i, g, p))
data.sort(key=lambda x: min(x[1], x[2]))
last_num = data[-1][0]
print(last_num)
k = 0
i = 0
while data[i][0] != last_num:
    _, g, p = data[i]
    if g < p:
        k += 1
    i += 1
print(k)
