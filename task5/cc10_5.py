def f(n):
    s1 = sum(filter(lambda x: x % 2 == 0, map(int, str(n))))
    s2 = sum(map(int, str(n)[1::2]))
    return abs(s1 - s2)


for i in range(1, 999_999):
    if f(i) == 17:
        print(i)
        break