'''Given a list of ints, 
return True if first and last number of a list is same'''

def last_first(numlist):
  firstnum = numlist[0]
  lastnum = numlist[-1]
  
  if firstnum == lastnum :
    print("The first number: ",firstnum,  "and" "last number: ", lastnum, "are same")
  else:
    print("The first and last numbers are not same")
    
numberlist = [10,20,30,40,50,60,10]
print("The result is", last_first(numberlist))
