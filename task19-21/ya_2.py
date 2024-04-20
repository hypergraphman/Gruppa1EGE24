def f(s, c, m):
    if s == 0:
        return c % 2 == m % 2
    if c >= m:
        return False
    moves = [f(s // 3, c + 1, m)]
    if s - 5 >= 0:
        moves.append(f(s - 5, c + 1, m))
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for s in range(1, 202 + 1):
    for m in range(1, 4 + 1):
        if f(s, 0, m):
            if m == 4:
                print(s)
            break
