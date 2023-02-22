
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

# Define a list of real numbers. Write a program that finds the difference between the maximum and minimum values of the fractional parts of the elements.

# Example:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def fructional_diff(list):
    fructional_list = []
    for number in list:
        x = round(number - int(number), 2)
        if x != 0:
            fructional_list.append(x)
    print(fructional_list)
    return max(fructional_list) - min(fructional_list)


our_list = [1.1, 1.2, 3.1, 5, 10.01]
print(fructional_diff(our_list))

# Write a program that will convert a decimal number to binary.

# Example:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def number_to_binary(n):
    binary_n = bin(n)
    binary_n = binary_n[2:]  # to remobe 0b from the string
    return binary_n


print(number_to_binary(45))
print(number_to_binary(3))
print(number_to_binary(2))
print(number_to_binary(101))


# Set a number. Make a list of Fibonacci numbers, including those for negative indices.

# Example:

# For k = 8, the list will look like this: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# Числа негафибоначчи определяются индуктивно следующим рекуррентным соотношением:

# F−1 = 1,
# F−2 = -1,
# Fn = F(n+2)−F(n+1).

def negaFibonacci(k):
    negaFibonacci_list = []
    a = 1
    b = 1
    for i in range(k - 1):
        a, b = b, a + b
        negaFibonacci_list.append(a)
    a = 0
    b = -1
    for i in range(k):
        a, b = b, a - b
        negaFibonacci_list.insert(0, a)

    return negaFibonacci_list


print(negaFibonacci(8))
