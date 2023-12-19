def f(n):
    d1, d2, d3 = map(int, str(n))
    s = sorted([d1 + d2, d2 + d3])[::-1]
    # res = ''.join(map(str, s))
    res = str(s[0]) + str(s[1])
    return res


for i in range(100, 1000):
    if f(i) == '145':
        print(i)




