from itertools import product


a = list(map(''.join, product(sorted('арсений'), repeat=6)))
for i, word in enumerate(a, start=1):
    temp = word.replace('е', 'а').replace('и', 'а').replace('с', 'р').replace('н', 'р').replace('й', 'р')
    if i % 2 == 0 and word[0] not in 'рс' and 'аа' not in temp and 'рр' not in temp:
        print(i, word)
