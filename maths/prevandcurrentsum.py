#Printing current and previous number sum in a given range

def previous(num):
  previousnum = 0
  for i in range (num):
    sum = previousnum +i
    print(sum)
    previousnum =i
  
print("Printing the current and previous number sum ")
previous(10)
