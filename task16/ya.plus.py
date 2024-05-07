from sys import setrecursionlimit

setrecursionlimit(3000)


def f(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return f(n - 1)
    return 6 * f(n - 1)


print(f(2049) // f(2046) // 3)
