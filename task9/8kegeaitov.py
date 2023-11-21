f = open('load.txt')

k = 0
for line in f.readlines():
    # a = list(map(int, line.split(';')))
    # a = [int(x) for x in line.split(';')]
    a = [int(x) for x in line.split(';')]
    # if odd in [2, 4]:
    #     k += 1
    if int((max(a) + min(a)) / 2 > sum(a) / len(a)) + int(sum(a[:3]) % 2 == 0 and sum(a[3:]) % 2 == 0) == 1:
        k += 1
print(k)
