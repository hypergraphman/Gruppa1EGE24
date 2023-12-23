def f(n):
    s1 = str(n)[::-1]
    s2 = ''
    for i in range(len(s1)):
        if i % 2 != 0:
            t = int(s1[i]) * 2
            if t > 9:
                t = t // 10 + t % 10
            s2 += str(t)
        else:
            s2 += s1[i]
    s3 = sum(map(int, s2))
    return s3 % 10 == 0


for i in range(1234_5678_9101_1122, 1234_5678_9101_1121 + 1000):
    if f(i):
        print(str(i)[-8:])
        break