

print('''

Write a Python program to sum all the items in a dictionary

''')

print()

import operator
d_colour = {'Red' : 10, 'Green' : 20, 'White':30, 'Purple': 40}

print(sum(d_colour.values()))
print(sorted(d_colour.items(),key=operator. itemgetter(0),))




print()
dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dict = {'d': 4, 'e': 5, 'f': 6, 'a': 1, 'b': 2, 'c': 3}

print(sum(dic.values()))
print(sum(dict.values()))

print(sum(dic.keys()))