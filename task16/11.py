from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 0:
         return 1
    if n > 0:
        return f(n - 1) * n


for i in range(1, 2025):
    f(i)
print(f(2025) / f(2023))