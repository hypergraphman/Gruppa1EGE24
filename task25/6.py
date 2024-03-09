import math
from functools import lru_cache


@lru_cache(None)
def sum_divs(n):
    p = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p.add(i)
            p.add(n // i)
    if len(p) == 0:
        return 0
    t = sorted(p)
    return t[0] + t[-1]


s = 0
k = 5
i = 777829
while k:
    if sum_divs(i) % 100 == 16:
        print(i, sum_divs(i))
        k -= 1
    i += 1
