print('''

Write a Python program which takes two digits m (row) and n (column) 
as input and generates a two-dimensional array. The element value in 
the i-th row and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1 
j = 0,1, n-1.

''')

print()

row_num = int(input("Number of rows you need: "))

col_num = int(input("Number of column you need :"))

multi_list = [[0 for col in range(col_num)] for row in range(row_num)]


for row in range(col_num):
    for col in range(row_num):
        multi_list [col] [row] = col*row
print(multi_list)
