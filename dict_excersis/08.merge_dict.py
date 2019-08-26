print('''


Write a Python script to merge two Python dictionaries
''')

print()

dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dict = {'d': 4, 'e': 5, 'f': 6, 'a': 1, 'b': 2, 'c': 3}

d = dic.copy()
d.update(dict)
print(d)