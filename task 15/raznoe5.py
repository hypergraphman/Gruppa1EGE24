for n in range(21, 100):
    k = 0
    for x in range(20, 91):
        A = (70 <= x <= 90)
        B = (15 <= x <= 50)
        C = (20 <= x <= n)
        f = int(((not A) <= B) and ((not C) <= A))
        if f:
            k += 1
            if k == 35:
                print(n)

