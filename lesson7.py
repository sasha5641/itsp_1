l = [1, 2, 3, 4, 5]
s = 'Hello'

l_iterator = iter(l)
s_iterator = iter(s)

print(next(l_iterator))
print(next(l_iterator))
print(next(l_iterator))

for el in l_iterator:
    print(el)

