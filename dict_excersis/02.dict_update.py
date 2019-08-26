print('''

Write a Python script to add a key to a dictionary. 

''')

print(


)

import operator

dict = {'d': 4, 'e': 5, 'f': 6, 'a': 1, 'b': 2, 'c': 3}

dict.update({'g':7,'h':8})

print(dict)

print("ascending order")
dict = sorted(dict.items(),key=operator.itemgetter(0))
print(dict)

print("Descending order")
dict = sorted(dict.items(),key=operator.itemgetter(0),reverse=True)
print(dict)

