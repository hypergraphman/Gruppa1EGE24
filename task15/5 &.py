k = 0
for a in range(1, 1000):
    if all(not (((x & 15 != 0) <= ((x & a != 0) <= (x & 108 != 0))) <= (x & 55 == 0) and (x & a != 0) and (x & 15 != 0)) for x in range(1, 1000)):
        print(a)
        k += 1
print(k)