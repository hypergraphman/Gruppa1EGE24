s1 = input()
s2 = input()
s3 = input()
if ' 0' in s1 and ' 0' in s2 and ' 0' in s3:
    if s1 > s2:
        s1, s2 = s2, s1
    if s2 > s3:
        s2, s3 = s3, s2
    if s1 > s2:
        s1, s2 = s2, s1
    print(s1 + ', ' + s2 + ', ' + s3)
elif ' 0' in s1 and ' 0' in s2:
    if s1 > s2:
        s1, s2 = s2, s1
    print(s1 + ', ' + s2)
elif ' 0' in s1 and ' 0' in s3:
    if s1 > s3:
        s1, s3 = s3, s1
    print(s1 + ', ' + s3)
elif ' 0' in s3 and ' 0' in s2:
    if s3 > s2:
        s3, s2 = s2, s3
    print(s3 + ', ' + s2)
elif ' 0' in s1:
    print(s1)
elif ' 0' in s2:
    print(s2)
elif ' 0' in s3:
    print(s3)