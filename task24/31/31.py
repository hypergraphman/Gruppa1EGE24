ALP = '0123456789ABCDEFGHIJKLMNOPQRST'
ODD = set(ALP[1::2])
EVEN = set(ALP[::2])


def check(number):
    if not number:
        return False
    s1, s2 = set(number[::2]), set(number[1::2])
    return s1 <= ODD and s2 <= EVEN or s1 <= EVEN and s2 <= ODD


def find_max_number(number, max_number):
    if number and number[0] != '0' and check(number):
        if len(number) > len(max_number):
            return number
        elif len(number) == len(max_number) and int(number, len(ALP)) < int(max_number, len(ALP)):
            return number
    return max_number


f = open('24.txt')
s = f.readline().strip() + '*'
number = ''
max_number = '0'
for c in s:
    if c in ALP:
        number += c
    else:
        max_number = find_max_number(number, max_number)
        number = ''
print(max_number)