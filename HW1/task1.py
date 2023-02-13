# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

# x = int(input('enter a weekday: '))
# if x >= 1 and x <= 5:
#     print("it's not a day off")
# elif x == 6 or x == 7:
#     print("it's a day off")
# else:
#     print("there is no such day of week")



# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# x= int(input('enter X: '))
# y= int(input('enter Y: '))
# z= int(input('enter Z: '))

# for x in [True,False]:
#     for y in [True,False]:
#         for z in [True,False]:
#             print(not (x or y or z) == (not x and not y and not z))



# """ Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится). 
# Пример: - x=34; y=-30 -> 4 - x=2; y=4-> 1 - x=-34; y=-30 -> 3 
# """


# def inputKoord(x):
#     a = [0] * x
#     for i in range(x):
#         is_OK = False
#         while not is_OK:
#             try:
#                 number = float(input(f"Введите {i+1} координату: "))
#                 a[i] = number
#                 is_OK = True
#                 if a[i] == 0:
#                     is_OK = False
#                     print("Координата не должно быть равна 0 ")
#             except ValueError:
#                 print("Ты ошибся. Вводить надо числа!")
#     return a


# def checkCoordinates(xy):
#     text = 4
#     if xy[0] > 0 and xy[1] > 0:
#         text = 1
#     elif xy[0] < 0 and xy[1] > 0:
#         text = 2
#     elif xy[0] < 0 and xy[1] < 0:
#         text = 3
#     print(f"Точка находится в {text} четверти плоскости")


# koordinate = inputKoord(2)
# checkCoordinates(koordinate)

""" Напишите программу, которая принимает на вход координаты двух точек 
и находит расстояние между ними в 2D пространстве. 
Пример: - A (3,6); B (2,1) -> 5,09 - A (7,-5); B (1,-1) -> 7,21 """


def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Ты ошибся. Вводить надо целые числа!")
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Введите координаты точки А")
pointA = inputNumbers(2)
print("Введите координаты точки В")
pointB = inputNumbers(2)

print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")