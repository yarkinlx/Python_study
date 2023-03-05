

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


# Calculate a number with a given accuracy d
# Example:

# at $d = 0.001, π = 3.141

# from math import pi
# print(pi)


# def pi_shorten(d):
#     str_d = str(d)
#     print(str_d)
#     print(len(str_d))
#     str_pi = str(pi)
#     return str_pi[:len(str_d)]


# print(pi_shorten(float(input('What accuracy is needed: '))))


# Define a natural number N. Write a program that will make a list of prime factors of number N.
# "20" -> [2, 2, 5]

def prime_factors_list(n):
    factor = 2
    prime_factors_list = []
    while n >= 2:
        if n % factor == 0:
            prime_factors_list.append(factor)
            n = n / factor
        else:
            factor +=1
    return prime_factors_list
        
print(prime_factors_list(int(input('enter a number: '))))