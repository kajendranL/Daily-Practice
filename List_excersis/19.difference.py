print('''Difference between the two lists''')


print()

def diff(lst1,lst2):
    return(list(set(lst1)-set(lst2)))





print("The numbers that are different are")
print(diff([1,2,3,4],[1,2]))
