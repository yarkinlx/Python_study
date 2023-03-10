# Арифметические операции
# - — вычитание
# * — умножение
# ** — возведение в степень
# / — деление
# // — целочисленное деление
# % — остаток от деления

print(8 / 2)   # => 4.0 (При делении двух чисел получается тип данных float)
print(3 ** 2)  # => 9
print(81/9)
print(80/9)
print(80//9)

a = 1.3
b = 3
print(a*b)
print(round(a*b))
c = round(a*b, 3)
print(c)
a += 3
print(a)

# Python: Приоритет
# Представим, что нужно вычислить такое выражение: 2 + 2 * 2. Именно так и запишем:

print(2 + 2 * 2)  # => 6
# В школьной математике есть понятие «приоритет операции». Приоритет определяет, в какой последовательности должны выполняться операции. Умножение и деление имеют больший приоритет, чем сложение и вычитание, а приоритет возведения в степень выше всех остальных арифметических операций. Например: 2 ** 3 * 2 вычислится в 16.

# Но нередко вычисления должны происходить в порядке, отличном от стандартного приоритета. Тогда приоритет нужно задавать круглыми скобками. Так было и в школе, например: (2 + 2) * 2. Скобки можно ставить вокруг любой операции. Они могут вкладываться друг в друга сколько угодно раз. Вот примеры:

print(3 ** (4 - 2))  # => 9
print(7 * 3 + (4 / 2) - (8 + (2 - 1)))  # => 14
# Главное при этом соблюдать парность — закрывать скобки в правильном порядке. Это часто становится причиной ошибок не только у новичков, но и у опытных программистов. Для удобства ставьте сразу открывающую и закрывающую скобку, а потом пишите внутреннюю часть. Редактор на нашем сайте (и большинство других редакторов кода) делают это автоматически: вы пишете (, а редактор сразу добавляет ). Это касается и других парных символов, например, кавычек. О них поговорим в будущих уроках.

# Иногда выражение сложно воспринимать визуально. Тогда можно расставить скобки, не повлияв на приоритет:

# Было
print(8 / 2 + 5 - -3 / 2)  # => 10.5

# Стало
print(((8 / 2) + 5) - (-3 / 2))  # => 10.5