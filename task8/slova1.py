from itertools import product

words = [''.join(word) for word in product('LICEY', repeat=4)]

print(len(words))