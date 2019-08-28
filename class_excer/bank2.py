import random
import sys

class Customer():
    bank_name = 'ABCBank'
    def __init__(self, name, id, balance = 0.0, annualInterestRate = 3.4):

        self.name = name
        self.id = id
        self.balance= balance
        self.annualInterestRate = annualInterestRate

    def getId(self):
        return self.id
    def getBalance(self):
        return self.balance
    def getAnnualInterestRate(self):
        return self.annualInterestRate
    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12
    def getMonthlyInterest(self):
        self.balance * self.getMonthlyInterestRate()
    def deposit(self,amt):
        self.balance = self.balance+amt
        print(('Balance after deposit' ,self.balance))
    def withdraw(self, amt):

        if amt>self.balance:
            print("In sufficient balance... cannot perform this operation")
            sys.exit()
        self.balance = self.balance-amt
        print("Balance after withdrawal", self.balance)




def main():
   # Creating accounts
   accounts = []
   for i in range(1000, 9999):
       account = Account(i, 0)
       accounts.append(account)
    
    while True:
        id = int(input("Enter your pin: "))

        while id <1000 or id >9999:
            
            id = int(input("Invalid id, please re-enter")
                 
        while True:
            print("1 - View Balance, 2 - Deposit, 3 - Withdraw, 4  - Exit")
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
       



https://www.engineeringbigdata.com/python-atm-code-for-account-balance-withdraw-and-deposit-functions/





