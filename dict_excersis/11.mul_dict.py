print('''


Write a Python program to multiply all the items in a dictionary
''')

print()

d_colour = {'Red' : 10, 'Green' : 20, 'White':30, 'Purple': 40}

result = 1

for i in d_colour:
    result = result * d_colour[i]


print(result)