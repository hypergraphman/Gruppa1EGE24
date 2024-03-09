from fnmatch import fnmatch

k = 0
for i in range(131, 10**8, 131):
    if fnmatch(str(i), '*13?*?1*'):
        k += 1
        if k % 1131 == 0:
            print(i, i // 131)