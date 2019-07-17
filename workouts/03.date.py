print('''Write a Python program to display the current date and time''')

import datetime

now = datetime.datetime.now()
print("The date and time is : ")
print(now.strftime("%Y/%m/%d %H: %M :%S"))
print(now.strftime("%Y-%m-%d %H: %M :%S"))
print(now.strftime("%Y.%m.%d %H: %M :%S"))

