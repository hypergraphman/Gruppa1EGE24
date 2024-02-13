from functools import lru_cache


@lru_cache(None)
def f(n, m):
    if m > n:
        return 0
    if m <= n and n % m == 0:
        return f(n, m + 1) + 1
    return f(n, m + 1)


for i in range(131131, 77, -1):
    f(131131, i)


print(f(131131, 77))

k = 0
for i in range(77, 131131 + 1):
    if 131131 % i == 0:
        k += 1
print(k)