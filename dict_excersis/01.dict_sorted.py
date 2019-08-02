print('''Write a Python script to sort (ascending and descending) a dictionary by value. ''')

print(


)

import operator
dict = {'d': 4,'e':5, 'f':6,'a':1, 'b':2,'c':3}

print("Original dict values")
print(dict)

print()
print("Ascending Order")
dict_1 =sorted(dict.items(),key = operator.itemgetter(0))
print(dict_1)

print()
print("descending order")

dict_2 = sorted(dict.items() , key = operator.itemgetter(0),reverse=True)

print(dict_2)
