
# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого


def check(a, b):
    if b/a == a or a/b == b:
        return "yes"
    else:
        return "no"


a = int(input("enter a: "))
b = int(input("enter b: "))

print(check(a, b))
