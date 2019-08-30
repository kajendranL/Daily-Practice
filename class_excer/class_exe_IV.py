
#Python Exercise 11 – binary  Number Divisible by 5
class divisible():

    def __init__(self):
        pass

    def divisible_binary(self,b):
        binary = []

        for i in b:
            conve = int(str(i),2)
            if conve % 5 == 0:
                binary.append(conve)
                print(i,end=',')
#Python Exercise 12 – 4 Digit Number Divisible by 4

    def div_4digit(self):
        div_4 = []

        for i in range(4000,9000):
            d = str(i)
            if (int(d[0]) % 4 == 0) and (int(d[1]) % 4 == 0) and (int(d[2]) % 4 == 0)and (int(d[3]) % 4 == 0):
                div_4.append(d)

        return div_4
    #each digit in the range is divisible by 4 and 8

    def div_4_and_8(self):
        div_4_8 = []
        for i in range(4000,9000):
            d = str(i)
            if (int(d[0]) % 4 == 0) and (int(d[1]) % 4 == 0) and (int(d[2]) % 4 == 0)and (int(d[3]) % 4 == 0):
                if(int(d[0])%8==0) and (int(d[1])%8==0)and (int(d[2])% 8 ==0) and (int(d[3])%8 ==0):
                    div_4_8.append(d)
        return div_4_8



di = divisible()
x = [1,10,11,100,110,111,1000,1001,1010,1011,1100,1110,1111,1000000,1000001,1000010,1000011,1000100,1000110,1000111,1001000,1001001,1001010,1001011,1001100,1001101,1001110,1001111,1010000,1010001,1010010,1010011,1010100,1010101,1010110,1010111,1011000,1011001,1011010,1011011,1011100,1011101,1011110,1011111,1100000,1100001,1100010,1100011,1100100]

print(di.divisible_binary(x))

print(di.div_4digit())
print(di.div_4_and_8())

