print(
    '''
    
    Write a Python program 
    to count the number of even and odd numbers from a series of numbers
    
    '''
)

print(


)
even = 0
odd = 0
num = (1,2,3,4,5,6,7,8,9,10)
for i in num:
    if i % 2:
        even +=1


    else:
        odd += 1

print("The count of even number is :", even)
print("The count of Odd number is : ", odd)
print()


num = (23)
count_even = 0
count_odd = 0

for i in range(num):
    if i % 2 == 0:
        count_even +=1
    else:
        count_odd += 1
print(count_even, " : is the count of even numbers in the given range",num)
print(count_odd, ":  is the count of odd numbers in the given range", num)