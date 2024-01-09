from itertools import product


a = list(map(''.join, product(sorted('кегэаитовру'), repeat=6)))
for i, word in enumerate(a, start=1):
    if i % 2 != 0 and word[0] != 'у' and word.count('к') == 2 and 'в' in word:
        print(i)
