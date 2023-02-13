

# 1. напишите программу которая принимает на вход вещественное число и показывает сумму его цифр:
# 0.56 = 11
# 12.56 = 14

a = input('Введите число ')


def summa(a):
    number = 0

    for i in str(a):
        if i != '.' and i != ',':
            number += int(i)
    return number


print(f'Сумма чисел равна {summa(a)}')


# 2. напишите программу, которая принимает на вход число n и выдает набор произведений числе от 1 до n
# n = 4 [1,2,6,24] - факториал

n = int(input('enter n: '))
f = 1
for i in range(1, n):
    f = f * i
    print(f, end=", ")

# 3. задайте список из k чисел последовательности(1+1/k)**k, и выведите их сумму

k = int(input('enter a number: '))
i = 1
sum = 0
k_list=[]
for k in range (i, k+1):
    temp = float((1+1/k)**k)
    sum +=temp
    k_list.append(temp)

print(k_list)   
print(f"sum of k's is {sum}")


# 4.  Задайте список из n элементов, заполненных числами из помежутка [-n; n]
# найдите произведение элементов на указанных пользователем через пробел позициях

def find_multiplication(n, positions):
    elements = [i for i in range(-n, n+1)]
    print(elements)
    product = 1
    for pos in positions:
        index = pos - 1
        if index < 0 or index >=len(elements):
            print(f"Error: position {pos} is out of range.")
            return None
        product *= elements[index]
    return product




n = int(input("Enter the value of N: "))
positions = list(map(int, input("enter the positions: ").strip().split()))
result = find_multiplication(n, positions)
if result is not None:
    print("the result of multiplication at the specified positions is: ", result)


# Реализуйте алгоритм перемешивания списка.

import random

def generate_random_list(n):
    random_list = []
    for i in range(n):
        random_list.append(random.randint(1,100))
    return random_list

def shuffle(*args):
    random.shuffle(random_list)
    return(random_list)

n = 10
random_list = generate_random_list(n)
print(random_list)
print(shuffle(random_list))