


class Maths_Excersise():

# find all such numbers which are divisible by 7 but are not a multiple of 5

    def find_range(self):
        l = []
        c = []

        for i in range(2000, 3201):
            if i % 7 == 0:
                l.append(i)
            elif i % 5 != 0:
                c.append(i)
        return l,c



#compute the factorial of a given numbers.
    def factorial(self,x):
        self.x = x
        if x == 0:
            return 1
        return x * self.factorial(x - 1)

#dictionary that contains (i, i*i)
    def  dict(self):
        d = dict()

        for i in range(1, x + 1):
            d[i] = i * i
        return d


#Method 1
me = Maths_Excersise()

print("The mumbers that are divisible by 7 are:", me.find_range())
print("The mumbers that are not divisible by 5 are:", me.find_range())

#method 2

x = int(input("Enter a number: "))
print(me.factorial(x))

#method _3

x = int(input("Enter a number: "))
print(me.dict())







