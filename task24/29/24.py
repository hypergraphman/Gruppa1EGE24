def find_max_number(number, max_number):
    if number and number[0] != '0' and number[-1] in '02468ACEGI':
        if int(number, 20) > int(max_number, 20):
            return number
    return max_number


f = open('24.txt')
s = f.readline()
number = ''
max_number = '0'
for c in s:
    if c in '0123456789ABCDEFGHIJ':
        number += c
    else:
        max_number = find_max_number(number, max_number)
        number = ''
max_number = find_max_number(number, max_number)
print(max_number)
