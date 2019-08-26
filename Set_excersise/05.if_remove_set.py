print('''
Write a Python program to remove an item from a set if it is present 
in the set. 

''')

print(

)


def if_remove(n):
    for i in n:
        if i in n:
            n.pop()

            print(i)

        return n


num = {44, 53, 65, 98, 78, 23, 24}

print("The given num removed", num.remove(53))
print(if_remove(num))

print(


)

num = {44, 53, 65, 98, 78, 23, 24}

num1= num.pop()
num2 = num.remove(78)
print("The given number", num2, "has been removed")
num3 = num.discard(24)
print("The given number",num3, "has been removed")