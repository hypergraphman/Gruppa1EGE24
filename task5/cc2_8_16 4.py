def f(n):
    s1 = f'{n:0>8b}'
    # t = ''.join([('0', '1')[el == '0'] for el in s1])
    t = ''.join([str(int(el == '0')) for el in s1])
    # t = ''
    # for el in s1:
    #     if el == '0':
    #         t += '1'
    #     else:
    #         t += '0'
    return int(t, 2)


for n in range(1, 255 + 1):
    r = f(n)
    if r - n == 131:
        print(n)