# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from cmath import sqrt


X1 = float(input('Введите координату X точки А = '))
Y1 = float(input('Введите координату Y точки А = '))
X2 = float(input('Введите координату X точки B = '))
Y2 = float(input('Введите координату Y точки B = '))

AB = sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
print(type(AB))
print(format(AB, '.2f'))