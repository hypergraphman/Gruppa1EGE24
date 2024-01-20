from itertools import product

words = [''.join(word) for word in product('kristna', repeat=3)]
words2 = [''.join(word) for word in product('lia', repeat=2)]
words3 = []
for word in words:
    for word2 in words2:
        words3.append(word + word2)
print(len(words3))