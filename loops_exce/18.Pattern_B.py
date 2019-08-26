for row in range(0, 6):
    for col in range(5):
        if row == 0 and col in {1, 2, 3}:
            print('A', end=' ')

        elif row in {1, 2, 4, 5, 6} and col in {0, 4}:
            print('A', end=' ')

        elif row == 3:
            print('A', end=' ')

        else:
            print(' ', end=' ')
    print()

print()

for row in range(7):
    for col in range(5):
        if row in {0, 3, 6} and col in {0, 1, 2, 3}:
            print('B', end=' ')
        elif row in {1, 2, 4, 5, } and col in {0, 4}:
            print('B', end=' ')
        else:
            print(' ', end=' ')
    print()

print()

for row in range(7):
    for col in range(5):
        if row in {0, 6} and col in {1, 2, 3}:
            print("C", end=' ')
        elif row in {1, 2, 3, 4, 5} and col == 0:
            print('C', end=' ')
        else:
            print(' ', end=' ')
    print()

print()

for row in range(7):
    for col in range(5):
        if row in {0, 6} and col in {0, 1, 2, }:
            print("D", end=' ')
        elif row in {1, 2, 3, 4, 5} and col in {1, 4}:
            print('D', end=' ')
        else:
            print(' ', end=' ')
    print()

print()

for row in range(7):
    for col in range(5):
        if row in {0, 6} and col in {0, 1, 2, 3, 4}:
            print('E', end=' ')
        elif row in {1, 2, 4, 5} and col == 0:
            print('E', end=' ')
        elif row == 3 and col in {0,1, 2, 3}:
            print('E', end=' ')
        else:
            print(' ', end=' ')
    print()
print()


for row in range(7):
    for col in range(5):
        if row in {0,3} and col in {1,2,3}:
            print("F", end=' ')
        elif row == 0 and col in {0,1, 2, 3, 4}:
            print("F", end=' ')
        elif row in {1,2,4,5,6}and col ==0:
            print('F', end=' ')

        else:
            print(' ',end=' ')

    print()

print()

for row in range(7):
    for col in range(5):
        if row in {0,6} and col in {0,1,2,3}:
            print('G',end=' ')
        if row in {3} and col in {2,3}:
            print('G',end=' ')
        elif row in {1,2,3,4,5} and col == 4:
            print('G', end=' ')
        elif row in {3,4,5,6} and col == 4:
            print('G', end=' ')


    print()