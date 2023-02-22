

list = [1, 2, 3, 4, 5]
print(round(len(list) / 2))
print(round(len(list) // 2))
print(round(2.5))
print(round(3.5))


# def Fibonacci(k):
#     Fibonacci_list = []
#     a = 0
#     b = 1
#     for i in range(k+1):
#         Fibonacci_list.append(a)
#         a, b = b, a + b
        
#     return Fibonacci_list

# print(Fibonacci(8))

n = int(input('Введите число: '))

def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = get_fibonacci(n)
print(get_fibonacci(n))
print(fibo_nums.index(0))

