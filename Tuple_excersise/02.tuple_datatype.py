print('''Write a Python program 
to create a tuple with different data types''')

print()

def tuple_with_diff_datatype(t):
    return t


datatype = (10,10.5, 3+4j, True, 'Kajendran', )

print("Tuple containing multiple data type")

print(tuple_with_diff_datatype(datatype))
print(type(datatype))