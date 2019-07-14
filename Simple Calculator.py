#Simple Calculator
num1=eval(input("Enter a number"))
oper=input("Enter an operation character")
num2=eval(input("Enter a second argument"))

if oper == '+':
    print("The output is:", num1, "+",num2,"=",num1+num2)
elif oper =='-':
    print("The output is:",num1,"-",num2,"=",num1-num2)
elif oper=='*':
    print("The output is:",num1,"*",num2,"=", num1*num2)
elif oper=='/':
    print("The output is:",num1/num2)
elif oper =='//':
    print("The output is:",num1//num2)
elif oper =='**':
    print("The output is:",num1**num2)
elif oper=='&':
    print("The output is:", num1 & num2)
elif oper =='^':
    print("The output is:", num1^num2)
elif oper =='<<':
    print("The output is:", num1<<num2)
else:
    print( "The operation character or the value entered is not correct, please correct your statements.")