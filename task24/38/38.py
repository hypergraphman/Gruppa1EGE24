from fnmatch import fnmatch

f = open('24.txt')
lines = f.readlines()
k = 0
for line in lines:
    if fnmatch(line, '*K??E*'):
        k += 1
print(k)

k = 0
for line in lines:
    for i in range(len(line) - 3):
        if line[i] == 'K' and line[i + 3] == 'E':
            k += 1
            break
print(k)
