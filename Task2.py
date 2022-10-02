# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

fracNum = float(input('Введите дробное число = '))
if fracNum%1 != 0:
    numFloat = (fracNum%1 *10)//1
    num = int(numFloat)
    print(num)
else:
    print('Нет')