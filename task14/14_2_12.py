for x in range(27):
    for y in range(27):
        a = 3 * 27 ** 8 + 1 * 27 ** 7 + x * 27 ** 6 + 1 * 27 ** 5 + 3 * 27 ** 4 + 1 * 27 ** 3 + y * 27 ** 2 + 1 * 27 ** 1 + 3 * 27 ** 0
        z = y * 27 + x
        if a % 26 == 0 and int(z ** 0.5) == z ** 0.5:
            print(z)