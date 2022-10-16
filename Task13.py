# Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random
def randList(length):
    number = []
    for i in range(length):
        number.append(random.randint(1,10))
    return number
N = int(input('Введите размер списка = '))
num = randList(N)
print(num)
neNum = 0
for i in range(N):
    if i%2 != 0:
        neNum += num[i]
print(num, " -> ", neNum)