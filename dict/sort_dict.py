import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print("Orginal dict: ", d)

sorted_d = sorted(d.items(), key = operator.itemgetter(0))

print("Dict in ascending order: ", sorted_d)

sorted_d = sorted(d.items(), key = operator.itemgetter(0),reverse = True)

print("dict in decending order: ", sorted_d)