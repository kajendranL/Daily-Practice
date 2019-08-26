print('''


Write a Python script to check if a given key already exists in a dictionary.

''')

print()

dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def is_key_present(x):
    if x in dic:
        print("The given  key is present in dic")
    else:
        print("No, The given key is not present")

is_key_present(5)
is_key_present(9)
is_key_present(3)