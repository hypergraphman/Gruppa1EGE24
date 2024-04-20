for a in range(1, 1000):
    if sum(not ((not (10 <= x <= 50) and (33 <= x <= 131)) <= (x > a)) for x in range(1, 1000)) == 42:
        print(a)

# for a in range(1, 1000):
#     k = 0
#     for x in range(1, 1000):
#         if not ((not (10 <= x <= 50) and (33 <= x <= 131)) <= (x > a)):
#             k += 1
#     if k == 42:
#         print(a)
