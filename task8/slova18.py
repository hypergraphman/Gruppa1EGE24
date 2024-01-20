from itertools import permutations

words = [''.join(word) for word in permutations('timur', r=4)]
res = []
for word in words:
    t = word.replace('m', 't').replace('r', 't').replace('u', 'i')
    if 'tt' not in t and 'ii' not in t:
        res.append(word)
print(len(res))