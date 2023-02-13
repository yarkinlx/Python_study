
# list = [8, 'hello', 7 , True]
# list.append(15)
# print(list)


# list = [8, 'hello', 7 , True]
# for i in list:
#     print(i, end=' ')


# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них


def check_max(a, b, c, d, e):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    if d > max:
        max = d
    if e > max:
        max = e
    return max


a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))
d = int(input('enter d: '))
e = int(input('enter e: '))

print(check_max(a, b, c, d, e))


# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

N = int(input('enter N: '))
ran = range(-N, N+1)
print(list(ran))

#  Напишите программу, которая будет на вход принимать дробь и показывать первую цифру дробной части числа:

# OPTION 1
a = float(input('enter a number: '))
b = a % 1
b = str(b)
print(b[2])

# OPTION 2

a = input('enter a number: ')
print(a.split('.')[1][0])

# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30

def check(a):
    if a % 5 == 0 and a % 10 == 0:
        return ('Число кратно 5 и 10')
    elif a % 15 == 0 and a % 30 != 0:
        return ('Число кратно 15, но не 30')
    else:
        return ('Число не подходит под оба варианта')


a = int(input('Enter a number: '))
print(check(a))
