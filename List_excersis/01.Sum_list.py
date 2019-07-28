print("Sum all the items in a list")

print()

def sum_list(items):

    sum_num = 0

    for i in items:
        sum_num +=i

    return sum_num

print("The sum of list are", sum_list([1,2,6,3,8,4,-6]))
print("The sum of list are", sum_list([1,2,5.8,6,-6]))
print("The sum of list are", sum_list([-7,-9,-5,-6]))
print("The sum of list are", sum_list([1,-9,-6,-8,-6]))