def is_color(color):
    # for c in color:
    #     if c not in '0123456789ABCDEF':
    #         return False
    if any(c not in '0123456789ABCDEF' for c in color):
        return False
    return color[2:4] < color[:2] > color[4:]


f = open('24.txt')
s = f.readline().strip()
k = 0
for i in range(len(s) - 7):
    if s[i] == '#':
        k += is_color(s[i + 1: i + 7])
print(k)