# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random
def randList(length):
    number = []
    for i in range(length):
        number.append(random.uniform(1,10))
    return number
N = int(input('Введите размер списка = '))
vesh = [round(c,3) for c in randList(N)]
min = 1
max = 0
for i in vesh:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i) 
print(vesh, '->', max-min)