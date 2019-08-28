
import sys

class Customer():
    bank_name = 'ABCBank'
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance= balance

    def deposit(self,amt):
        self.balance = self.balance+amt
        print(('Balance after deposit' ,self.balance))
    def withdraw(self, amt):

        if amt>self.balance:
            print("In sufficient balance... cannot perform this operation")
            sys.exit()
        self.balance = self.balance-amt
        print("Balance after withdrawal", self.balance)

print("Welcome to", Customer.bank_name)

name = input("Enter your name: ")

cust = Customer(name)
while True:
    print("1 - Deposit, 2 - Withdraw, 3  - Exit")
    option = input("Enter your option: ")
    if option == '1' :
        amt = eval(input("Enter the amount to deposit: "))
        cust.deposit(amt)
    elif option == '2' :
        amt = eval(input("Enter the amount to withdraw:"))
        cust.withdraw(amt)
    elif option == '3' :
        print("Thank you for banking with us")
        sys.exit()
    else:
        print("Invalid operation please try again")


