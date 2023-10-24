b1 = 131
b2 = 25
b3_s = 176
b3_e = 183
b4_s = 0
b4_e = 255
count = 0
for b3 in range(b3_s, b3_e + 1):
    for b4 in range(b4_s, b4_e + 1):
        adress = f'{b1:x}.{b2:x}.{b3:x}.{b4:x}'
        if '5' in adress:
            count += 1
print(count)