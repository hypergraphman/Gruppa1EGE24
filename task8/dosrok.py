from itertools import product

words = [''.join(x) for x in product(sorted('ШАТЕР'), repeat=5)]
for i, word in enumerate(words, start=1):
    if word.count('А') <= 1 and 'ЕЕ' not in word:
        print(i, word)
        break