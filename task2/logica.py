ans1 = ''
ans2 = ''
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = int(a and (not b and not c or b and c) or a and (b and not c or not b and c))
            g = int(a)
            ans1 = ans1 + str(f)
            ans2 = ans2 + str(g)
print(ans1)
print(ans2)