print('''

Write a Python program which iterates the integers from 1 to 50. 
For multiples of three print "Fizz" instead of the number and 
for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".

''')

print()

num = 50

for i in range(50):
    if i % 3 == 0 and i % 5 ==0:
        print("FizzBuzz")
        continue

    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    print(i)


