

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

# def prime_factors_list(n):
#     factor = 2
#     prime_factors_list = []
#     while n >= 2:
#         if n % factor == 0:
#             prime_factors_list.append(factor)
#             n = n / factor
#         else:
#             factor +=1
#     return prime_factors_list
        
# print(prime_factors_list(int(input('enter a number: '))))


# Define a sequence of numbers. Write a program that outputs a list of non-repeating elements of the original sequence.


# def unrepeated_sequence(seq):
#     unique_elements = []
#     for element in seq:
#         if seq.count(element) == 1:
#             unique_elements.append(element)
#     return unique_elements

# sequence = [1,1,2,3,4,5,5]
# print(unrepeated_sequence(sequence))


# A natural degree k is given. Randomly generate a list of coefficients (values from 0 to 100) of a polynomial and write the polynomial of degree k to a file.
# Example:

# k=2 => 2*x² + 4*x + 5 = 0 or x² + 5 = 0 or 10*x² = 0


# import random

# k = 2
# coefficients = [random.randint(0,100) for i in range(k + 1)]
# with open(file = 'polynomial.txt', mode = 'w') as file:
#     polynomial = ''
#     for i, coef in enumerate(coefficients):
#         if coef == 0:
#             continue
#         elif i == 0:
#             polynomial += f"{coef}"
#         elif i == 1:
#             polynomial += f"{'+' if coef > 0 else '-'}{abs(coef)}x"
#         else:
#             polynomial += f"{'+' if coef > 0 else '-'}{abs(coef)}x^{i}"
#     file.write(polynomial)

# with open(file = 'polynomial.txt', mode = 'r') as file:
#     polynomial = file.read()

# print(f"`the polynomial of degree{k} is: {polynomial}")


# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random

k = 2
coefficients = [random.randint(0,100) for i in range(k + 1)]

with open(file = 'polynomial.txt', mode = 'w') as file1:
    polynomial = ''
    for i, coef in enumerate(coefficients):
        if coef == 0:
            continue
        elif i == 0:
            polynomial += f"{coef}"
        elif i == 1:
            polynomial += f"{'+' if coef > 0 else '-'}{abs(coef)}x"
        else:
            polynomial += f"{'+' if coef > 0 else '-'}{abs(coef)}x^{i}"
    file1.write(polynomial)

coefficients = [random.randint(0,100) for i in range(k + 1)]

with open(file = 'polynomial2.txt', mode = 'w') as file2:
    polynomial = ''
    for i, coef in enumerate(coefficients):
        if coef == 0:
            continue
        elif i == 0:
            polynomial += f"{coef}"
        elif i == 1:
            polynomial += f"{'+' if coef > 0 else '-'}{abs(coef)}x"
        else:
            polynomial += f"{'+' if coef > 0 else '-'}{abs(coef)}x^{i}"
    file2.write(polynomial)

with open(file = 'polynomial.txt', mode = 'r') as file1:
    polynomial = file1.read()
with open(file = 'polynomial2.txt', mode = 'r') as file2:
    polynomial2 = file2.read()

with open(file = 'polynomial.txt', mode = 'r') as file1:
    coefficients1 = list(map(int, file1.read().split()))
with open(file = 'polynomial2.txt', mode = 'r') as file2:
    coefficients2 = list(map(int, file2.read().split()))

if len(coefficients1)> len(coefficients2):
    coefficients2 += [0] * (len(coefficients1) - len(coefficients2))
else:
    coefficients1 += [0] * (len(coefficients2) - len(coefficients1))

sum_coefficient = [coef1 + coef2 for coef1, coef2 in zip(coefficients1, coefficients2)]

print(f"`the first polynomial1 of degree {k} is: {polynomial}")
print(f"`the second polynomial1 of degree {k} is: {polynomial2}")


with open('polynomial_sum.txt', 'w') as file3:
    polynomial_sum = ''
for i, coef in enumerate(sum_coefficient):
    if coef == 0:
            continue
    elif i == 0:
            polynomial_sum += f"{coef}"
    elif i == 1:
            polynomial_sum += f"{'+' if coef > 0 else '-'}{abs(coef)}x"
    else:
            polynomial_sum += f"{'+' if coef > 0 else '-'}{abs(coef)}x^{i}"
    file3. write(polynomial_sum)
print(f"`the sum of polynomials is: {polynomial_sum}")