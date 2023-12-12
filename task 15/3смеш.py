for x in 1, 7:
    for a in range(1, 200):
        d42 = 42 % x == 0
        d35 = 35 % x == 0
        f = (d42 <= (not d35)) <= (3 * x + a < 131)
        if not f:
            print(a)