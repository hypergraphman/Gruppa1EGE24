from fnmatch import fnmatch


def f(n):
    a = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return sorted(a)


def fi(n):
    return len(f(n)) == 2


for i in range(1700000, 1, -1):
    if fnmatch(str(i), '*131*?'):
        if not fnmatch(str(i), '*9*'):
            c = 0
            s = 0
            fu = ''
            for j in f(i):
                if fi(j):
                    c += 1
                    fu += str(j)
            if c >= 3:
                for k in fu:
                    s += int(k)
                print(i, s)
