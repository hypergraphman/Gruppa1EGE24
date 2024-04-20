k = 0
for a in 126, 1364:
    is_a = True
    for x in range(1000):
        for y in range(1000):
            f = int(((x <= 10) or (x**3 + 3 * x >= a) and ((y * y + 5 * y <= a) or (y >= 10))))
            if not f:
                is_a = False
    if is_a:
        k += 1
print(k)