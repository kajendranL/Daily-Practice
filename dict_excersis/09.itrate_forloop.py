print('''

Iterate over dictionaries using for loops

''')

print()

d_colour = {'Red' : 10, 'Green' : 20, 'White':30, 'Purple': 40}

for key, value in d_colour.items():
    print(key, "corresponds to" , d_colour[key])