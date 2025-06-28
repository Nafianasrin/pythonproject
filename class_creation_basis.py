
class car:
    def display_details(self,brand,model,year):
        print("car:",brand,model,year)
a=car()
b=car()
a.display_details("Toyota","Corolla",2020)
b.display_details("Tesla","Model 3",2023)



"""
class car:
    def __init__(self):
        self.brand=input("Enter the brand name ")
        self.model=input("Enter the model name ")
        self.year=int(input("enter the year "))

    def display_details(self):
        print("Your car is of brand:",self.brand,",model:",self.model,",year:",self.year)
a=car()
a.display_details()
"""