for a in range(1, 10000):
    is_a = True
    for x in range(1, 200):
        d8 = x % 8 == 0
        d6 = x % 6 == 0
        if not ((d8 <= (not d6)) or (x + 2 * a > 100)):
            is_a = False
    if is_a:
        print(a)
        break
