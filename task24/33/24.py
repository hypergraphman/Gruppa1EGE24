a = [len(x) for x in open('24.txt').readline().strip().split('Q')]
mx = 0
for i in range(len(a) - 4):
    mx = max(mx, sum(a[i: i + 4]))
print(mx + 3)