print('''
Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence. Go to the editor
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010

''')

print()

items = []

num = [x for x in input().split(',')]

for i in num:
    a = int(i,2)
    if not a %5:
        items.append(i)
print(items)

