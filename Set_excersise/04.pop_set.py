print(''' 

Remove items from Python set
''')

print()

def remove_set(n):
    i=0

    while i < len(n):

        n.pop()
        i+=i
        return n



num = {11,2,22,33,44,55,66,}

print(remove_set(num))
print(remove_set(num))
print(remove_set(num))
print(remove_set(num))
print(remove_set(num))
print(remove_set(num))
print(remove_set(num))