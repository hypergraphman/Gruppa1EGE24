for a in range(0, 100):
    if all(((x <= 60) <= (x <= a)) and ((y * y <= a) <= (y <= 8)) for x in range(1, 100) for y in range(1, 100)):
        print(a)
print('--------------')
for a in range(0, 100):
    is_a = True
    for x in range(0, 100):
        for y in range(0, 100):
            if not (((x <= 60) <= (x <= a)) and ((y * y <= a) <= (y <= 8))):
                is_a = False
    if is_a:
        print(a)