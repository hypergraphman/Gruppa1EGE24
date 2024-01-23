from itertools import product

words = [''.join(word) for word in product('01234', repeat=5) if len(set(word)) == 4 and word[0] != '0']
res = []
for word in words:
    if '00' not in word and '11' not in word and '22' not in word and '33' not in word and '44' not in word:
        res.append(word)
print(len(res))