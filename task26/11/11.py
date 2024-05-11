f = open('26.txt')
n = int(f.readline())
data = []
for x in f:
    el = x.split()
    data.append((int(el[0]), eval(f'{el[0]} - 2 * {el[1]}')))
data.sort(key=lambda x: -x[1])
package = [data[0]]
for out, inner in data:
    _, t_inner = package[-1]
    if t_inner - 3 >= out:
        package.append((out, inner))
print(len(package))
limit_out = package[-2][1] - 3
mx = 0
for out, _ in data:
    if mx < out <= limit_out:
        mx = out
print(mx)