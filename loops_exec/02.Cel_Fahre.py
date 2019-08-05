print ('''Convert temperatures to and from celsius, fahrenheit)''')

print()

temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")

degree = int(temp[:-1])
i_convert = temp[-1]

if i_convert.upper() == 'C':
  result = int(round((9*degree)/ 5+32))
  o_convert = 'Fahrenheit'
elif i_convert.upper() =='F':
  result = int(round((degree - 32)* 5 /9))
  o_convert = 'Celsius'
else:
  print("Input proper convention.")
  quit()
  
print("The temperature in", o_convert, "is", result, "degrees")
