print('''
Write a Python function to reverse a string if it's 
length is a multiple of 4

''')

print()

def len_mult_4(str):
    if len(str) % 4 == 0:
        return ''.join(reversed(str))
    return str

print(len_mult_4('abcd'))
print(len_mult_4('1234'))
print(len_mult_4('python'))
