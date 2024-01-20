from itertools import product

words = [''.join(word) for word in product('DILYRA', repeat=6) if word.count('D') == 1 and word.count('R') == 1 and word.count('I') <= 1]
print(len(words))
