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



print()

import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print("The original values of Dict",d)

print("Ascending order: ")
d1=sorted(d.items(), key=operator.itemgetter(0))

print (d1)

d2 = sorted(d.items(),key=operator.itemgetter(0), reverse = True)
print("Descending order")
print(d2)