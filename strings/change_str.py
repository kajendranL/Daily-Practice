
print('''Write a Python program to change a given string to a new string 
where the first and last chars have been exchanged''')

print()

def change_spl_char(str1):
    return str1[-1] +str1[1:-1]+str1[:1]

print(change_spl_char('python'))