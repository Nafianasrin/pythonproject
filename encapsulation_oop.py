"""
it contains attributes and methods in a single class. data hiding. other classes cannot access the attributes
and methods. we create private attribute by using _ or __ .

#example
class product:
    def __init__(self):
        self.__price=900 # '__' represents it is private.
    def printprice(self):
        print("the price of the product is ",self.__price)
    def setprice(self,price):
        self.__price=price

a=product()
a.printprice()
a.__price=1000 #in a normal program, this will help to set the price as 1000 without calling the setprice().
               #but here it is not allowed.
a.printprice()
a.setprice(1000)
a.printprice()
"""
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
        print("current bank balance :",self.balance)
        self.deposit=int(input("Enter the amount to be deposited "))
        self.balance=self.balance+self.deposit
        ch=int(input("do you want to withdraw?"))
        if ch==1:
            self.withdraw=int(input("enter the amount "))
            self.balance=self.balance-self.withdraw
        else:
            self.withdraw=0
    def deposits(self):
        print("Deposited :",self.deposit)
    def withdraws(self):
        print("Withdrawn :",self.withdraw)
    def checkbalance(self):
        print("Balance :",self.balance)
a=BankAccount(5000)
a.deposits()
a.withdraws()
a.checkbalance()