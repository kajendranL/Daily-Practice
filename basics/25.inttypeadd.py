print("Write a Python program to add two objects if both objects are an integer type")

print()

def inttypeadd(a,b):
    if not isinstance(a, int) and isinstance(b,int):
        raise TypeError ("Inputs must be integers")
    return a+b

print(inttypeadd(13,12))
print(inttypeadd('a', 2))