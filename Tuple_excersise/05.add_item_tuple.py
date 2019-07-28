print('''Write a Python program to add an item in a tuple. ''')

print()


def add_item_tuple(t1):
    return t1


num = (10, 10.5, (3 + 4j), True, 'Kajendran')
num2 = ("epifano",)

print("The concatenation of the two tuples are")
print(add_item_tuple(num + num2))

##########OR OR OR OR OR ###########

print()

# creating a tuple with the value

tu = (4, 5, 6, 3, 1)
print(tu)
print(id(tu))
# tuples are immutable, so you can not add new elements
# using merge of tuples with the + operator you can add an element and it will create a new tuple
print()
print("Concateneted")
tu = tu + (9,)
print(tu)
print(id(tu))

# adding items in a specific index
print()
tu = tu[:5] + (10, 5, 30) + tu[:5]
print(tu)
print(id(tu))

#converting the tuple to list
print()
lst = list(tu)
lst.append(100)
tu = tuple(lst)
print(tu)
print(type(tu))