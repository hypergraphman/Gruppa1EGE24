for a_l in range(-20, 20):
    is_a = True
    for a_r in range(100, a_l, - 1):
        is_a = True
        for x in range(-1000, 1000):
            if not (((x * x <= 20) <= (a_l <= x <= a_r)) and ((a_l <= x <= a_r) <= (x * x <= 144))):
                is_a = False
        # print(a_l, a_r)
        if is_a:
            print(a_l, a_r)