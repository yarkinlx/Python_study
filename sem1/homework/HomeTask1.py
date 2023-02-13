# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# a = int(input('enter a number of weekday: '))
# if 1<=a<=5:
#     print("it's not a weekend")
# elif 6<=a<=7:
#     print("it's a day off")
# else:
#     print("the number is out of range")

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in range(0,1):
#     for y in range(0,1):
#         for z in range(0,1):
#             print((not (x or y or z) == (not x and not y and not z)))

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)

# def check_quarter(x, y):
#     if x > 0 and y > 0:
#         return 'the point is in 1st quarter'
#     elif x < 0 and y > 0:
#         return 'the point is in 2nd quarter'
#     elif x < 0 and y < 0:
#         return 'the point is in 3rd quater'
#     elif x > 0 and y < 0:
#         return 'the point is in 4th quarter'
#     else:
#         return 'zero value can\'t be used'


# x = int(input('enter x: '))
# y = int(input('enter y: '))

# print(check_quarter(x, y))

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

# def value_check(a):

#     if a == 1:
#         return "x(0;+∞), y(0;+∞)"
#     elif a == 2:
#         return "x(0;-∞), y(0;+∞)"
#     elif a == 2:
#         return "x(0;-∞), y(0;+∞)"
#     elif a == 3:
#         return "x(0;-∞), y(0;-∞)"
#     elif a == 4:
#         return "x(0;+∞), y(0;-∞)"
#     else:
#         return 'the number is out of range'

# a = int(input("enter a quarter number: "))
# print(value_check(a))



# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
# AB = √((xb - xa)2 + (yb - ya)2).
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

a = float(input('введите значение точки А по X: '))
b = float(input('введите значение точки А по Y: '))
c = float(input('введите значение точки B по X: '))
d = float(input('введите значение точки А по Y: '))

from math import sqrt

# value= ((c-a)**2) + ((d - b)**2)
# distance = round(value**0.5, 2)
distance = round(sqrt(((c-a)**2) + ((d - b)**2)),2)
print(distance)

