f = open('26.txt')
n = int(f.readline())
data = []
for line in f:
    data.append(tuple(map(int, line.split())))
data.sort(key=lambda x: x[1])
room = [data[0][1]]
for s, e in data:
    if s >= room[-1]:
        room.append(e)
print(len(room))
for s, e in data[::-1]:
    if s >= room[-2]:
        print(e)
        break
