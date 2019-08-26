print('''
Write a Python program to remove a key from a dictionary.
''')

print()

d_colour = {'Red' : 10, 'Green' : 20, 'White':30, 'Purple': 40}

print(d_colour)

if 'Red' in  d_colour:
    del d_colour['Red']

print(d_colour)
