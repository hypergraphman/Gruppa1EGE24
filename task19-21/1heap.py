def f(s, c, m, k):
    if s >= 203:
        return c % 2 == m % 2
    if c > m:
        return False
    moves = [f(s + 1, c + 1, m, 0),
             f(s + 2, c + 1, m, 0)]
    if k == 0:
        moves.append(f(s * 3, c + 1, m, 1))
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


count = 0
for s in range(1, 202 + 1):
    for m in range(1, 4 + 1):
        if f(s, 0, m, 0):
            if m == 3:
                count += 1
            print(s, m)
            break
print(count)