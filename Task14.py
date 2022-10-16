# Напишите программу, которая найдёт произведение пар чисел списка (CСписок создаем как в предыдущем задании). Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
def randList(length):
    number = []
    for i in range(length):
        number.append(random.randint(1,10))
    return number
N = int(input('Введите размер списка = '))
number = randList(N)
numberSum = []
for i in range(N//2):
    numberSum.append(number[i]*number[-(i+1)])
print(number, '->', numberSum)