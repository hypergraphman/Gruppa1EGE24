def f(n):
    s1 = f'{n:b}'
    s2 = s1[:-1]
    if n % 2 != 0:
        s3 = s2 + '10'
    else:
        s3 = s2 + '01'
    return int(s3, 2)


for i in range(1000, 2000):
    if f(i) == 2025:
        print(i)
        break