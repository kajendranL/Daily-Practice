print('''
 Write a Python program to create the colon of a tuple
 
 ''')

print()

from copy import deepcopy

def colon_tuple(n):
    for i in n:
        tup_colon = deepcopy(tup)
        tup_colon[3].append(50)
        print(tup_colon)
    return tup


tup = (10, 10.5, (3+4j), [], True, 'Kajendran', 'epifano')
print(colon_tuple(tup))


