print("Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn")

print()

a = int(input("Enter a number: "))

n1 = int("%s" %a)
n2 = int("%s%s" %(a, a))
n3 = int("%s%s%s" %(a, a, a))

print("The value is: ", n1+n2+n3)

