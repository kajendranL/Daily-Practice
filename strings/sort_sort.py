print('''Write a Python program to sort a 
string lexicographically''')

print()

def lexi_sort(s):
    return sorted(sorted(s), key=str.upper)

print(lexi_sort('w3resource'))
print(lexi_sort('genesistraining'))