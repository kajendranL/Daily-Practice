print('''
Write a Python program to construct the following pattern, 
using a nested for loop

''')
print()

n=8
for i in range(n):
    for j in range(i+1):
        print("*",end = '')
    print()

for i in range(n,0, -1):
    for j in range(i-1):
        print("*",end='')
    print()
print("***********************************************")
for i in range(n):
    for j in range(i+1):
        print("*",end = '')
    print()

for i in range(n,0, -1):
    for j in range(i-1):
        print("*",end='')
    print()
    