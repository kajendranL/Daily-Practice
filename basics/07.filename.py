print('''Write a Python program to accept a filename from the user and print the extension of that''')

filename = input("Enter the name of the file")

f_extens = filename.split(".")
print("The file extension is", f_extens[-1])