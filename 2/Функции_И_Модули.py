
"""
def new_string(symbol, count):
    return symbol * count


print(new_string('Q', 12))
"""

def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', "s", "d", "f"))
print(concatenatio('a', 'q')) 