print('''

Write a Python script to print a dictionary where the keys are 
numbers between 1 and 15 (both included) and the values are square of keys

''')

print()

s = {}
def squr_keys(d):
    for x in range(d):
        s[x]=x**2
    print(s)


n = int(input("Enter a key : "))

print(squr_keys(n))

c = int(input("Enter a key : "))
print(squr_keys(c))

