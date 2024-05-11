f = open('26.txt')
n, l, m = map(int, f.readline().split())
car = [0] * l
van = [0] * m
data = []
for line in f:
    s, d, t = line.strip().split()
    s = int(s)
    e = s + int(d)
    data.append((s, e, t))
data.sort()
v_count = 0
not_p_count = 0
for s, e, t in data:
    p = False
    if t == 'A':
        for i in range(len(car)):
            if car[i] <= s:
                car[i] = e
                p = True
                break
        if not p:
            for i in range(len(van)):
                if van[i] <= s:
                    van[i] = e
                    p = True
                    break
    else:
        for i in range(len(van)):
            if van[i] <= s:
                van[i] = e
                p = True
                v_count += 1
                break
    if not p:
        not_p_count += 1
print(v_count, not_p_count)