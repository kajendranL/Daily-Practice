print('''

Write a Python program to iterate over dictionaries using for loops
''')

print()

dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for key, value in dic.items():
    print(key, "->", value)
    