#Python Exercise 8 – User Input a List and Sort Alphabetically

class sort_words():
    def __init__(self):
        pass

    def words_split(self,s):
        s.sort()
        return s

    print()

    #Python Exercise 8 –User Input Sentences and Print Input as Upper Case

    def upper_case(self,s):
        sentences = []
        while True:
            if s:
                sentences.append(s.upper())
                break
            else:
                break
        for i in sentences:
            print(i)

    print()

    #Python Exercise 10 – Remove Duplicate Words with User Input

    def remove_dupe(self,w):
        word_list=[]
        [word_list.append(s) for s in w if s not in word_list]
        return word_list

    def binary(self, b):
        binary_list=[]
        for i in b:
            conve = int(str(i),2)
            if conve % 5 == 0:
                binary_list.append(conve)

                print(i,end=',')
            else:
                binary_list.append(conve)
        return #Output is wrong



sw = sort_words()
print("Ordered")
print()
x = ['tornado','hurricane','tsunami','flood','thunderstorm','hail','rain','wind']
print(sw.words_split(x))

print("Upper cased")
print()
s = """In this Python exercise, write a Python program that will 
    accept a few sentences as input from a user and print the 
sentences in upper case after user input. Take a look into the 
upper case function in Python and how to store values 
from user input"""
print(sw.upper_case(s))
print()
print("Remove dupelicate")
print()
print(' '.join(sw.remove_dupe(s.split())))

b = [1,10,11,100,110,111,1000,1001,1010,1011,1100,1110,1111,1000000,1000001,1000010,1000011,1000100,1000110,1000111,1001000,1001001,1001010,1001011,1001100,1001101,1001110,1001111,1010000,1010001,1010010,1010011,1010100,1010101,1010110,1010111,1011000,1011001,1011010,1011011,1011100,1011101,1011110,1011111,1100000,1100001,1100010,1100011,1100100]
print(sw.binary(b))







