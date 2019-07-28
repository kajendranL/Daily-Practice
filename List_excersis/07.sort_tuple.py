print('''Write a Python program to get a list, sorted in increasing order by the last element 
in each tuple from a given list of non-empty tuples.''')

print()

def last (n): return n[-1]


def sort_last_list(tuples):
    return sorted(tuples, key=last)


print(sort_last_list([(2,5),(3,4),(6,3),(9,2),(7,1)]))