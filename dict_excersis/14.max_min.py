print('''

Write a Python program to get the maximum and minimum value in a dictionary

''')



d_colour = {'Red' : 10, 'Green' : 20, 'White':30, 'Purple': 40}

key_max = max(d_colour.keys(),key=(lambda k : d_colour[k]))
key_min = min(d_colour.keys(),key=(lambda k : d_colour[k]))

print("The Max Value is ", key_max)
print("The min Value is ", key_min)



print()

#?????

my_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])