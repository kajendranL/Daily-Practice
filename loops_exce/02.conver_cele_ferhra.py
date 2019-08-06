print('''

Write a Python program to convert temperatures to and from celsius, 
fahrenheit. Go to the editor
[ Formula : c/5 = f-32/9 
[ where c = temperature in celsius and f = temperature in fahrenheit ] 
''')

print()

temp = input("Enter the temprature you want to convert to (ex: 40F or 30C): ")

degree = int(temp[:-1])
i_convert = temp[-1]

if i_convert.upper() == 'C':
    result = int(round((9*degree)/5+32))
    o_convert = 'Fahrenheit'

elif i_convert.upper() == 'F':
    result = int(round((degree-32)*5/9))
    o_convert = 'Celsius'

else:
    print("input in right format")
    quit()


print("The tempreture in ",o_convert, "is", result,"degree")
