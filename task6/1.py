from turtle import *

# fd = forward- вперед
# bk = back - назад
# rt = right - направо
# lt = left - налево
# speed - скорость работы черепахи
# goto - перемещение на нужную позицию
# pu = penup - поднять хвост
# pd = pendown - опустить хвост
# dot - нарисовать точку
# done - чтобы после рисования черепаха не закрывалась

speed(0)
scale = 20
for _ in range(2):
    fd(13 * scale)
    rt(90)
    fd(20 * scale)
    rt(90)
pu()
fd(8 * scale); rt(90); bk(3 * scale); lt(90)
pd()
for _ in range(2):
    fd(16 * scale)
    rt(90)
    fd(8 * scale)
    rt(90)

pu()
for x in range(29):
    for y in range(4, -21, -1):
        goto(x * scale, y * scale)
        dot(4, 'Red')

done()