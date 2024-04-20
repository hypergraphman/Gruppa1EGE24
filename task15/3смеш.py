for a in range(1, 10000):
    if all(((42 % x == 0) <= (35 % x != 0)) or (3 * x + a < 131) and (a % 4 == 0) for x in range(1, 10000)):
        print(a)