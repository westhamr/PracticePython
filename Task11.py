# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

num = int(input('Введите число = '))
list = []
for i in range(1, num+1):
    list.append(round((1+1/i)**i, 3))
print(round(sum(list), 3))