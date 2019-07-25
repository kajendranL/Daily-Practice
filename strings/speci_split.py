print(''' 

Write a Python program 
to get the last part of a string before 
a specified character.''')


print()

str = "https://www.w3resource.com/python-exercises/string"

print("The result is", str.rsplit('/',1)[0])
print("The result is",str.rsplit('-',1)[0])

