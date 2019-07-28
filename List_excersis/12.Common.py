print('''Write a Python function that takes two lis
ts and returns True if they have at least one common member''')

print()

def common_member(lst1, lst2):
    result =  False

    for x in lst1:
        for y in lst2:
            if x == y:
                result = True
                return result





list1 = [10,20,30,40,50]
list2 = [60,70,80,90,20]

print(common_member(list1, list2))
print(common_member([1,2,3,4,5], [5,6,7,8,9]))
print(common_member([1,2,3,4,5], [6,7,8,9]))