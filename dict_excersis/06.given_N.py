print('''


Write a Python script to generate and print 
a dictionary that contains a number (between 1 and n) in the form (x, x*x)

''')

print()

n = int(input("Enter a number : "))

d = {}

for x in range(n):
    d[x] = x*x
print(d)

