from fnmatch import fnmatch

for i in range(2025, 10**9 + 1, 2025):
    if fnmatch(str(i), '1?31*437?'):
        print(i, i // 2025, sep='*', end='-')