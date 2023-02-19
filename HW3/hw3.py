
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def find_odd_position_sum(list):
    odd_position_sum = 0
    for i in range(len(list)):
        if i % 2 != 0:
            odd_position_sum += list[i]
    return odd_position_sum


our_list = [2, 3, 5, 9, 3, 5]
print("The sum of elements in odd positions is:",
      find_odd_position_sum(our_list))


# Write a program that finds the product of pairs of numbers in a list. Pairs are the first and last element, the second and penultimate, etc.

# Example:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def product_of_pairs(list):
    i = 0
    o = -1
    prod_list = []
    # for i in range(((len(list) // 2))):
    if len(list) % 2 == 1:
        while i < len(list) // 2 + 1:
            product = list[i] * list[o]
            prod_list.append(product)
            i += 1
            o -= 1
    else:
        while i < len(list) // 2:
            product = list[i] * list[o]
            prod_list.append(product)
            i += 1
            o -= 1

    return prod_list


task_list = [1, 2, 3, 4, 5]
task_list_2 = [2, 3, 5, 6]
task_list_3 = [1, 2, 3, 4, 5, 6]
task_list_4 = [1, 2, 3, 4, 5, 6, 7]
print('the product of pairs of numbers in a list is :',
      product_of_pairs(task_list))
print('the product of pairs of numbers in a list is :',
      product_of_pairs(task_list_2))
print('the product of pairs of numbers in a list is :',
      product_of_pairs(task_list_3))
print('the product of pairs of numbers in a list is :',
      product_of_pairs(task_list_4))

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def fructional_diff(list):
    fructional_list = []
    for number in list:
        x = round(number - int(number), 2)
        fructional_list.append(x)
    print(fructional_list)
    return max(fructional_list) - min(fructional_list)

our_list = [1.1, 1.2, 3.1, 5.02, 10.01]
print(fructional_diff(our_list))