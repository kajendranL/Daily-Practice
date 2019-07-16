'''Accept string from the user and display only those characters
which are present at an even index'''

def evenindexchr(string):
  for i in range(0,len(string)-1,2):
    print("The index of [",i,"] is",string[i])
    
inputstr = input("Enter a string of your choice: ")
print("Original string is: ",inputstr)

print("Strings at even index are: ")
print(evenindexchr(inputstr))
