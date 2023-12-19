from itertools import permutations


def f(n):
    d1, d2, d3 = str(n)
    a = [d1 + d2, d1 + d3, d2 + d1, d2 + d3, d3 + d1, d3 + d2]
    b = set([int(x) for x in a if x[0] != '0'])
    # b = []
    # for x in a:
    #     if x[0] != '0':
    #         b.append(x)
    # a = set(filter(lambda x: x[0] != '0', map(lambda x: ''.join(x), permutations(str(n), r=2))))
    # b = list(map(int, a))
    return max(b) - min(b)


for n in range(100, 1000):
    if f(n) == 80:
        print(n)