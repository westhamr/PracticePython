# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

floatNum = input('Введите вещественное число = ')
symbol = '-,.'
for char in symbol:
    floatNum = floatNum.replace(char, "")
print(sum(map(int, list(floatNum))))

