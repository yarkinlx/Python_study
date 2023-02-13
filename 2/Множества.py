'''

colors = {'red', 'green', 'blue'}
print(type(colors))
colors.add('red')
print(colors)
colors.add('pink')
print(colors)
colors.remove('red')
colors.discard('red')
colors.clear()
print(colors)

'''

a = {1,2,3,5,8}
b = {2,5,8,13,21}
c = a.copy()
u = a.union(b)
i = a.intersection(b)
dl = a.difference(b)
dr = b.difference(a)

print(a)
print(b)
print(c)
print(u)
print(i)
print(dl)
print(dr)


q = a \
    .union(b) \
    .difference(a.intersection(b))

s = frozenset(a)