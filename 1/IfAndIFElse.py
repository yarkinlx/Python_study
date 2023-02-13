# # Условная конструкция (if)

# def get_type_of_sentence(sentence):
#     last_char = sentence[-1]
#     if last_char == '?':
#         return 'question'
#     return 'normal'

# print(get_type_of_sentence('Hodor'))   # => normal
# print(get_type_of_sentence('Hodor?'))  # => question


# a = int(input('a = '))
# b = int(input('b = '))

# if a>b:
#     print('a is higher')
# elif a==b:
#     print('equal')
# else:
#     print('b is higher')



def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    elif last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'Sentence is ' + sentence_type

print(get_type_of_sentence('Who?'))  # => 'Sentence is question'
print(get_type_of_sentence('No'))    # => 'Sentence is normal'
print(get_type_of_sentence('No!'))   # => 'Sentence is exclamation'