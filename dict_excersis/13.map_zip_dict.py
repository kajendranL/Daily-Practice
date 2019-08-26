print('''

Write a Python program to map two lists into a dictionary
''')

print()

keys = ['Red', 'White', 100]

values = [10, 30, 'Purple']

d_colour = dict(zip(keys,values))
print(d_colour)