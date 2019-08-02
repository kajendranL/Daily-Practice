print('''Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.''')

print()

num = input("Enter some numbers please")

list = num.split(",")


tuple = tuple(list)
set = set(list)

print("List = ",list)
print()
print("Tuple = ",tuple)
print()
print("set = ",set)
