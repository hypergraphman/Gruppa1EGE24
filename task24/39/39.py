from collections import Counter
from string import digits, ascii_uppercase


def alina_count(s):
    k = 0
    for i in range(len(s) - 4):
        if s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4] == 'ALINA':
            k += 1
    return k


def count(s):
    k = 0
    for i in range(len(s) - 2):
        if s[i] in digits and s[i + 1] in digits and s[i + 2] in ascii_uppercase:
            k += 1
    return k


lines = open('24.txt').readlines()
find_line = lines[0]
max_alina = 0
find_i = 0
for i in range(len(lines)):
    k = alina_count(lines[i])
    if k >= max_alina:
        max_alina = k
        find_line = lines[i]
        find_i = i

print(Counter(find_line))
k = 0
for i in range(find_i, len(lines)):
    k += lines[i].count('K')
print('K' + str(k))