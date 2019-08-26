class findout():

    def __init__(self,s,d):
        self.s  = s
        self.d = d
        def odd_even(self):

            if self.s % 2 == 0:
                print("The given number is even")
            else:
                print("The given number is odd")

        def div_by(self):

            if self.s % 4==0:
                print("The given number is multiple of 4")

        def div_4(self):

            if self.s % self.d == 0:
                print("The given number is divisible by ",d)
            else:
                print("The given number is not divisible by:", d)



num = int(input())
num1 = int(input())
n = findout(num, num1)






