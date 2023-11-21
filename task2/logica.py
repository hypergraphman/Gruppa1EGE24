print('a b c f')
ans1 = ''
ans2 = ''
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = int(not ((not (not a and c)) and not (not b and c)))
            g = int(not (a and b) and c)
            ans1 = ans1 + str(f)
            ans2 = ans2 + str(g)
print(ans1)
print(ans2)