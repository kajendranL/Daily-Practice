print("Write a Python program to calculate number of days between two dates")

print()

from datetime import date

f_date = date(2019, 7, 11)
l_date = date(2019, 7, 25)

delta = l_date - f_date

print("The days difference is", delta.days)