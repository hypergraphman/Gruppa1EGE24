f = open('24.txt')
line = f.readline()
max_odd_number = 0
s = 0
is_number = False
for i in range(len(line)):
    if not is_number and line[i].isdigit():
        is_number = True
        s = i
    elif is_number and not line[i].isdigit():
        is_number = False
        num = int(line[s:i])
        if num % 2 != 0 and num > max_odd_number:
            max_odd_number = num
print(max_odd_number)
