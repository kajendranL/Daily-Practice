# Write your code below and hit run.
class my_myth():
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b:
            return a / b

        else:
            return ("Can't be divided by zero")

    def pow(self, a, b):
        return a ** b


a1 = my_myth()

print(a1.add(3, 3))
print(a1.sub(3, 3))
print(a1.mul(3, 3))
print(a1.div(3, 3))
print(a1.div(0, 3))
print(a1.div(3, 0))
print(a1.pow(3, 3))