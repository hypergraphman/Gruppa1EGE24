f = open('26_2615_1.txt')
n, *a = map(int, f)
a.sort()
s = 0
k = 0
for el in a:
    if el - 1 <= s:
        s += el
        k += 1
    else:
        print(s + 1, k)
        break
