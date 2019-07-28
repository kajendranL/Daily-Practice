print('''Write a Python program to unpack a 
tuple in several variables''')

print()


def unpack_tuple(t):

    return t



t1 = (10, 10.5, (3 + 4j), True, 'Kajendran')

a, b, c, d, e = t1
print(unpack_tuple(t1))
print(a)
print(b)
print(c)
print(d)
print(e)

