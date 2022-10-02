# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

num = int(input("Введите число = "))
numList = range(-num, num+1)
numListRange = list(numList)
print(numListRange)