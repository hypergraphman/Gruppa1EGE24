ans1 = ''
ans2 = ''
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = int((a <= b) and (c <= b))
            g = int((a and c) <= b)
            ans1 = ans1 + str(f)
            ans2 = ans2 + str(g)
print(ans1)
print(ans2)