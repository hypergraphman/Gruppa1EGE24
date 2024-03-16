f = open('24.txt')
s = f.readline() + '+'
q = ""
ans = "0"
an = '0123456789ABCDEFGHI'
for i in s:
    if i in an:
        q += i
    else:
        if q:
            if (q[0] != '0') and (int(q, len(an)) % 2 == 0) and (int(q, len(an)) > int(ans, len(an))):
                ans = q
        q = ''
print(ans)
