data = []
with open('26.txt') as f:
    n, s = map(int, f.readline().split())
    for _ in range(n):
        cost, t = f.readline().split()
        cost = int(cost)
        data.append((cost, t))
data.sort()

k = 0
z = []

for i in range(n):
    cost, t = data[i]
    if s - cost >= 0:
        s -= cost
        if t == 'Z':
            z.append(cost)
        else:
            k += 1
    else:
        if t == 'Q':
            if s + z[-1] - cost >= 0:
                s = s + z.pop() - cost
                k += 1
print(k, s)
