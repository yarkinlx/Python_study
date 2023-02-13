"""
a = int(input('enter a: '))
b = int(input('enter b: '))

if (a/b==b or b/a==a):
    print('yes, it is square')
else:
    print('no it is not square')

"""

# списки


# my_list = [8,'r',7, True]
# # my_list.append('end') #добавить в конец списка
# # my_list.pop([1]) # удаляет элемент из списка
# # my_list.remove([2]) # удаляет элемент из списка
# # print(my_list[-1])
# # print(my_list[2])

# print(len(my_list))


# range(5)   -> [0,1,2,3,4]
# range(1,11) -> [1,2,3,4,5,6,7,8,9,10]
# range(1,10,2) -> [1,3,5,7,9]

# цикл

# my_list = [8,'r',7, True]
# for item in my_list:
#      print(item, end = ' * ')


# my_list = [8,'r',7, True]
# for i in range(len(my_list)):
#     print(my_list[i])


# ЗАДАЧА 1
# программу которая на вход принмает 5 чисел и находит максимальное их них
# 1,4,8,7,5
# 78,55,36,90,2

# my_list = (78,55,36,9,2)
# i = 1
# max = my_list[0]
# while(i<5):
#     if my_list[i] > max:
#         max = my_list[i]
#         i=i+1
#     else:
#         i+=1
# print (max)

# length = 5
# my_list = []
# for i in range(length):
#     my_list.append(int(input('enter number: ')))
# print(my_list)
# print(max(my_list))
# # max_number = my_list[0]
# # for i in range(1,length):
# #     if max_number < my_list[i]:
# #         max_number = my_list[i]

# # print(max_number)


# Задача 2
# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# n = int(input('enter the number: '))
# for i in range(-n, n+1):
#     print(i, end = ' ')

# Задача 3
# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# x = float(input())
# print(int(x*10) % 10)

# x = input()
# print(x.split('.')[1][0])

# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно (5 и 10) или (15, но не 30)

n = int(input("enter the number: "))
# print(n/5)
# print(n//5)
# print(n%5)

if ((n % 5 == 0) and (n % 10 == 0)) or ((n % 15 == 0) and (n % 30 != 0)):
    print(" число кратно (5 и 10) или (15, но не 30)")
else:
    print("no")
