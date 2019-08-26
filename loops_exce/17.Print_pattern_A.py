print('''
Write a Python program to print alphabet pattern 'A'.

''')

print()

for row in range(0, 6):
    for col in range(5):
        if row == 0 and col in {1, 2, 3}:
            print('*', end=' ')

        elif row in {1, 2, 4, 5, 6} and col in {0, 4}:
            print('*', end=' ')

        elif row == 3:
            print('*', end=' ')

        else:
            print(' ', end=' ')
    print()

star = ''

for row in range(7):
    for col in range(7):
        if (((col == 1 or col == 5) and row != 0) or ((row == 0 or row == 3) and (col < 1 and col > 5))):
            star = star + "*"
        else:
            star = star + '  '
    star = star + "\n"
print(star)

print()

c= 0
for i in range(7):
    if i %3 == 0 and c<2:
        print(5*"*")
        c+=1
    else:
        print("*   *")