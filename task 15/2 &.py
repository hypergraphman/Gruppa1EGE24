for a in range(1, 1000):
    if all((((x & 26 != 0) or (x & a != 0)) <= (x & 26 != 0)) or ((x & a != 0) and (x & 79 == 0)) for x in range(1, 1000)):
        print(a)