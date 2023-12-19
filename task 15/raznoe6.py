my_set = set()
for n in range(0, 55):
    k = 0
    for x in range(0, 91):
        P = (25 <= x <= 40)
        Q = (37 <= x <= 50)
        C = (n <= x <= 54)
        f = (P <= Q) and ((not C) <= Q)
        if f:
            k += 1
            if k > 25:
                my_set.add(n)
                break
print(max(my_set))