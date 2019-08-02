print('''Write a Python program which accepts the radius of a circle from the user and compute the area''')

from math  import pi

r = int(input("Enter the radius :"))
print("The radius of ", r, "is", pi*r**2)
