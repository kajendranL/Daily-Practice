print('''Write a Python program to convert a tuple to a string.''')

print()



lst = (10, 10.5, (3+4j), True, 'Kajendran', 'epifano')
print("The original tuple is ")
print(lst)
print(type(lst))
lst = str(lst)
print()
print('The tuple converted to string')
print(lst)
print(type(lst))
print()




print("Converted to sting and joined letters")
lst2 = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(lst2)

print()
print(str)