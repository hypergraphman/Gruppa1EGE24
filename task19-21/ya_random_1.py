def f(s1, s2, c, m):
    if s1 == s2:
        return c % 2 == m % 2
    if c >= m:
        return False
    if s1 > s2:
        moves = [f(s1, s2 + 1, c + 1, m),
                 f(s1, s2 + 2, c + 1, m)]
    else:
        moves = [f(s1 + 1, s2, c + 1, m),
                 f(s1 + 2, s2, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for s in range(1, 30 + 1):
    for m in range(1, 4 + 1):
        if f(15, s, 0, m):
            if m == 4:
                print(s)
            break
