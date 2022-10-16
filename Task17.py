# Задайте число - размер списка. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
num = int(input('Введите число  = '))
list = []
for i in range(1, num + 1):
    list.append(Fibonacci(i))
neglist = list.copy()
for i in range(num):
    neglist[i] *= -1
neglist[::-1] + list
print(neglist[::-1] + list)