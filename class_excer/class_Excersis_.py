# Python Exercise 3 Problem

class big_data():   # class

    def __init__(self):   # constrctor
        pass
    def dict_x(self, x):     # method
        x_dict = dict()       # x = local variable
        for x in range(1, x + 1):
            x_dict[x] = x * x
        return x_dict
    #Python Exercise 4 – Generate a List and Tuple with User Input

    def list_tuple(self,x):
        lst = x.split(',')
        tup = tuple(lst)

        return lst, tup

    # Python Exercise 5 – Define a Class with Two Methods

    def getcolour(self):
        self.colour = ""  # instance variable
        self.colour = input("What is your favourite colour?  ")
        print(f"\nYour favourite colour is {self.colour.upper()}")
        return self.colour

    #Python Exercise 6 Problem

    def grocery_item(self):
        items = input("Please list some of the items from your grocery list..(make sure they are seperated by commas")

        items = [x for x in items.split(',')]
        items.sort()
        return items





bd = big_data()
print(bd.dict_x)
x = int(input("Enter a number"))
print(f"\nyou have entered an integral of {x}")

print(f"\nThe integral number of {x} produced the below with the {x}, {x}*{x}:")
print(bd.dict_x(x))

print(bd.list_tuple)
x= input("Enter a sequence of number divided by comas:  ")

print(f"\nThis is a printed list and tuple of the number values: ")
print(f"\t{bd.list_tuple(x)} ")

print(bd.getcolour())
print(bd.grocery_item())



