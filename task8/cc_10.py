from itertools import product


a = list(map(''.join, product(sorted('ластик'), repeat=5)))
k = 0
for word in a:
    temp = word.replace('и', 'а').replace('с', 'л').replace('т', 'л').replace('к', 'л')
    if 'аа' not in temp and 'лл' not in temp and (word < 'касса' or word > 'такса'):
        k += word.count('т')
print(k)
