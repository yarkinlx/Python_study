
# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.


#  Set a string of a set of numbers. Write a program that shows the higher and the lower numbers. Use a space as the separator character.

# string = "11 2 3 4 5 6"

# our_list = string.split()
# number_list = list(map(int, our_list))
# print(number_list)
# print(max(number_list))
# print(min(number_list))

import numpy as np
from math import sqrt


def find_high_low(number_string):
    number_list = number_string.split(' ')
    number_list = list(map(int, number_list))
    highest = max(number_list)
    lowest = min(number_list)
    return f'highest is {highest} and lowest is {lowest}'


number_string = input("Enter a string of numbers separated by spaces: ")
print(find_high_low(number_string))


# 2. Find the roots of the quadratic equation Ax² + Bx + C = 0 in two ways:
# 1) Using mathematical formulas to find the roots of a quadratic equation
# 2) with the help of additional Python libraries


def quadratic_equation(a, b, c):
    discriminant = (b**2) - (4 * a * c)
    if discriminant < 0:
        return 'there no roots, D < 0'
    elif discriminant == 0:
        x = (-b + 0) / (2 * a)
        return f'D = 0, the only root is {x}'
    else:
        x_1 = (-b + sqrt(discriminant)) / (2 * a)
        x_2 = (-b - sqrt(discriminant)) / (2 * a)
        return f'x_1 is {x_1}, x_2 is {x_2}'


a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))
print(quadratic_equation(a, b, c))
# −4x2 + 28x — 49 = 0
# 3x2— 4x+94 = 0
# x2— 10 = 39


# input coefficients
A = float(input("Enter the coefficient of x^2: "))
B = float(input("Enter the coefficient of x: "))
C = float(input("Enter the constant term: "))

# create an array of coefficients
coefficients = np.array([A, B, C])

# calculate the roots using numpy.roots function
roots = np.roots(coefficients)

# print the roots
print("The roots are", roots[0], "and", roots[1])
#
#
# Note: The numpy.roots function returns an array of complex roots. If the roots are real, the imaginary part of the complex roots will be 0.


# Define two numbers. Write a program that finds the least common multiple of these two numbers.
# lcm(a, b) = (a * b) / gcd(a, b)

def find_lcm(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    lcm = (a*b) / gcd(a, b)
    return f'least common multiple is {lcm} '


a = int(int(input('enter first number: ')))
b = int(int(input('enter second number: ')))

print(find_lcm(a, b))
