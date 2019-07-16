'''Given a list of numbers, Iterate it 
and print only those numbers which are divisible of 5'''

def divisible5(n):
  for i in n:
    if i % 5 == 0:
      print(i)
      
      
numlist= 10,40,28,39,50,45,69,65,38

print("From the given list these are the nubmers that are divisible by 5")
divisible5(numlist)
