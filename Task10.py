# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input('Введите число = '))
factorial = 1
for i in range(2, num+1):
    factorial *= i
    print(factorial, end=', ')
