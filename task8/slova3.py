from itertools import product

words = [''.join(word) for word in product('камиль', repeat=6) if word[0] != 'ь' and word.count('м') == 1]
print(len(words))

# words = [''.join(word) for word in product('камиль', repeat=6)]
# res = []
# for word in words:
#     if word[0] != 'ь' and word.count('м') == 1:
#         res.append(word)
# print(len(res))
