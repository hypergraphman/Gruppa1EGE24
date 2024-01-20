from itertools import product

words = [''.join(word) for word in product('ЭЛИНА', repeat=5)]
res = []
for word in words:
    t = word.replace('И', 'Э').replace('А', 'Э').replace('Н', 'Л')
    if 'ЭЭ' not in t and 'ЛЛ' not in t:
        res.append(word)
print(len(res))