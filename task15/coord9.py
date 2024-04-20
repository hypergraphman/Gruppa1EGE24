for a in range(100, 200):
    if all(((x >= a) or (2 * y >= a)) <= (y + 5 * x != 70) for x in range(1000) for y in range(1000)):
        print(a)
        break

for a in range(100, 200):
    is_a = True
    for x in range(1000):
        for y in range(1000):
            f = ((x >= a) or (2 * y >= a)) <= (y + 5 * x != 70)
            if not f:
                is_a = False
                break
        if not is_a:
            break
    if is_a:
        print(a)
        break