

original = 645
inverted = 0
# print(original % 10)
while original !=0:
    inverted = inverted * 10 + (original % 10)
    original //=10
else:
    print('Пожалуй, хватит')
print(inverted)

list = [1,2,3,4,5]
for i in list:
    print(i**2)


list = range(10)
for i in list:
    print (i**2)



for i in range(10):
    print (i**2)


for i in range(1,10,2):
    print (i)



for i in 'qwertyuiop':
    print (i)

