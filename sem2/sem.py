

# i = 1
# while i < 11:
#     print(i, end=" ")
#     i += 1


# 1. напишите программу, которая принимаеи на вход число n и выдает последовательность из n членов

"""""
n = int(input('enter a number: '))

a = 1
i=1

while (i < n+1):
    print(a, end=', ')
    a *= (-3)
    i+=1
"""""
# 2. для натурального n создать, состоящий из элементов последовательности 3n+1
"""""
n = int(input('enter a number: '))
i = 1

for n in range (i, n+1):
    print(f"{i}: {3*n+1}")
    i+=1
"""""
#
# напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другую


# str1 = input("введите строку 1: ")
# str2 = input("введите строку 2: ")

# count = str1.count(str2)

# print(f'{str2} occurs {(count)} times in {str1}')

string1 = 'Я люблю Питон!'
string2 = 'лю'
count = 0

for i in range(0, len(string1)):
    if string1[i: i + len(string2)] == string2:
        count += 1

print(count)
