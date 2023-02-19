

# реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел

import random
'''
def generate_random_list(n):
    random_list = []
    for i in range(n):
        random_list.append(random.randint(1,100))
    return random_list


print(generate_random_list(10))
print(generate_random_list(10))
'''

# def generate_random_list(n):
#     random_list = []
#     x = 123456789
#     y = 362436069
#     z = 521288629
#     w = 88675123

#     for i in range(n):
#         t = x ^ (x << 11)
#         x, y, z = y, z, w
#         w = w ^ (w >> 19) ^ (t ^ (t >> 8))
#         random_list.append(w % 100)

#     return random_list

# print(generate_random_list(11))

# задайте список. напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# [['efg23', '79234gefg', 'sdgs', 'g53']
# '2'
# ['efg23', '79234gefg']


# def look_for_i(our_list, searchable):

#     result_string = []

#     for i in our_list:
#         if searchable in i:
#             result_string.append(i)

#     return result_string


# print(look_for_i(['efg23', '79234gefg', 'sdgs', 'g53'], '2'))


# 3. Напишите программу, которая определит позицию второго вхождения
# строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


# def find_second_occurrence(lst, string):
#     try:
#         # find the index of the first occurrence of the string in the list
#         first_occurrence = lst.index(string)
#         # find the index of the second occurrence of the string in the list
#         second_occurrence = lst.index(string, first_occurrence + 1)
#         return second_occurrence
#     except ValueError:
#         # the string does not occur in the list or occurs only once
#         return "String does not exist or occurs only once in the list"

# # Example usage:
# lst = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# string = "йцу"
# second_occurrence = find_second_occurrence(lst, string)
# print(second_occurrence) # Output: 3

def find_second_occurrence(list, string):
    first_occurrence = 0
    for i in range(len(list)):
        if list[i] == string:
            first_occurrence = i
            break
    
    second_occurrence = 0
    for i in range(first_occurrence + 1, len(list)):
        if list[i] == string:
            second_occurrence = i
            break
    if second_occurrence == 0:
        return 'the string does not occur in the list or occurs only once'
    else:
        return second_occurrence


list = ["йцу", "фыв", "йцу", "цук", "йцукен", "poi"]
string = "йцу"
print(find_second_occurrence(list,string))
