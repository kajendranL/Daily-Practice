


d= {1: 2, 6: 9, 10: 15, 20: 25, 30: 35}

d1 = {100: 'Yazh', 300: 'Epi'}

d1[600] = 'Amala'

d.update(d1)
print(d)

print()

import operator


print("Ascending Order")
d1 = sorted(d.items(), key=operator.itemgetter(0))

print(d1)


print()
print("Descending order")
d2 = sorted(d.items(), key=operator.itemgetter(0), reverse= True)
print(d2)
