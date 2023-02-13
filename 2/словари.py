
# Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу

dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→',
    }

print(dictionary)
print(dictionary['left'])

for k in dictionary.keys():
    print(k)

for v in dictionary.values():
    print(v)
