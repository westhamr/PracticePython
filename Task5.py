# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = int(input('Введите x = '))
Y = int(input('Введите y = '))
Z = int(input('Введите z = '))
param = [X,Y,Z]

check = (not(X or Y or Z)) == (not X and not Y and not Z)
print(check)