from itertools import permutations

words = [''.join(word) for word in permutations('alina')]
res = set()
for word in words:
    if 'aa' not in word:
        res.add(word)
print(len(res))