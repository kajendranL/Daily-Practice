print('''Write a Python program to get the 4th element and 4th element 
from last of a tuple''')

print()

def nth_element(tup):
    print(tup[3] , tup[-4])



lst = (10, 10.5, (3+4j), True, 'Kajendran', 'epifano')
print(nth_element(lst))