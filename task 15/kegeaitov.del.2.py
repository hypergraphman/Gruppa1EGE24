for a in range(1, 100):
    if all((x % a == 0) or ((x % 35 == 0) <= (x % 49 == 0)) for x in range(1, 1000)):
        print(a)
print('-----------------')
for a in range(1, 100):
    is_a = True
    for x in range(1, 1000):
        if not ((x % a == 0) or ((x % 35 == 0) <= (x % 49 == 0))):
            is_a = False
    if is_a:
        print(a)