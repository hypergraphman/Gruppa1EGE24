for a in range(1, 5000):
    if all((x > 15) or (y > 25) or (2 * y + 3 * x < a) for x in range(0, 5000) for y in range(0, 5000)):
        print(a)
        break