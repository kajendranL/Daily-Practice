print(

    '''Write a Python function to convert a given string 
to all uppercase if it contains 
at least 2 uppercase characters in 
the first 4 characters'''
      )

print()

def to_upper(str):
    num_uppper = 0
    for i in str [:4]:
        if i.upper() == i:
            num_uppper +=1
    if num_uppper >= 2:
        return str.upper()
    return str

print(to_upper('python'))
print(to_upper('Python'))
print(to_upper('pyThon'))
print(to_upper('PyThon'))
print(to_upper('pythoN'))