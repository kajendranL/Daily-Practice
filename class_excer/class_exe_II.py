# 2-dimensial Array

# pattern drawing

class pattern():
    def __init__(self):
        pass

    def array_2_dimen(self,x):

        self.rownum = x[0]
        self.column = x[1]
        multi = [[0 for col in range(self.column)] for row in range (self.rownum)]


        for row in range(self.rownum):
            for col in range(self.column):
                multi[row][col]= row*col
            return multi
    print()

pa=pattern()
x = [5,7]
print(pa.array_2_dimen(x))
# the above code needs to be worked upon

