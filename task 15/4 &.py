for a in range(45, 65 + 1):
    is_a = True
    for x in range(1, 10000):
        nz30 = x & 30 != 0
        nz10 = x & 10 != 0
        z10 = x & 10 == 0
        nz108 = x & 108 != 0
        za = x & a == 0
        nz21 = x & 21 != 0
        f = ((nz30 <= nz10) or nz108) <= (z10 and za and nz21)
        if f:
            is_a = False
    if is_a:
        print(a)