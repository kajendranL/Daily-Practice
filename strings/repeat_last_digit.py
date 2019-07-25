print('''Write a Python function to get a string made of 4 copies of the 
last two characters of a specified string (length must be at least 2).''')

print()

def repeat_digits(str):
    sub_str = str[-2:]
    return sub_str * 4

def repeat_first(str1):
    sub_str1 = str1[:2]
    return sub_str1 * 4


print(repeat_digits('python'))
print(repeat_digits('Epifano'))

print()
print(repeat_first('python'))
print(repeat_first('Epifano'))