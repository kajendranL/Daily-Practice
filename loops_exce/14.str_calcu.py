print('''

Write a Python program that accepts a string and calculate the number of 
digits and letters. Go to the editor
Sample Data : Python 3.2
Expected Output :
Letters 6 
Digits 2
''')

print()
alpha_count = 0
num_count=0
sample_data = input("Enter a string")


for  i in sample_data:
    if i.isalpha():
        alpha_count= alpha_count+1
    if i.isdigit():
        num_count = num_count+1
print("Alphapets are: ", alpha_count)
print("Numbers are :",num_count)




