from fnmatch import fnmatch

for i in range(47, 10**10, 47):
    t = str(i)
    if fnmatch(str(i), '9*4*0') and all(t[x] > t[x + 1] for x in range(len(t) - 1)):
        print(i, i // 47)