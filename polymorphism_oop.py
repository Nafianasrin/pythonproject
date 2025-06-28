class Dog:
    def speak(self):
        print("Dog says woof!")
class Cat:
    def speak(self):
        print("Cat says meow!")
dog=Dog()
dog.speak()
cat=Cat()
cat.speak()

"""
it means many forms. types==> method overloading,method overriding,operator overloading,duck typing
"""
#method overloading: name of () same, but diff attribute inside the same class
# class A:
#     def area(self,a=0,b=0):
#         if a!=0 and b!=0:
#            print("area of a rect will be ",a*b)
#         elif a!=0:
#            print("area of square will be ", a*a)
#         else:
#            print("specify the length and breadth")
#
# obj=A()
# obj.area()
# obj.area(2)
# obj.area(2,3)


#method overriding:inheritance
# class A:
#     def fun1(self):
#         print("function 1")
#     def fun(self):
#         print("function from parent") #if the child doesnt have fun(), then it will execute this fun()
# class B(A):
#     def fun3(self):
#         print("function 3")
#     def fun(self):
#         print("function from child") #overrides
#         super().fun() #this will help to call fun() from parent
# obj=B()
# obj.fun1()
# obj.fun3()
# obj.fun()


#operator overloading: we can overload +,-,*, etc
# class product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def __add__(self, other): #operator overloading +
#         print("add is working")
#         total=self.price+other.price
#         print("added",total)
#     def __sub__(self, other): #operator overloading -
#         print("sub is working")
#         total=self.price-other.price
#         print("subtracted",total)
#     def __mul__(self, other): #operator overloading
#         print("mul is working")
#         total=self.price*other.price
#         print("multiple",total)
# p1=product("box",20)
# p2=product("lunchbox",40)
# p1 + p2 # it only possible when operator overloads, o.w shows errors
# p1 - p2
# p1 * p2


#Duck typing: any animal that behaves like duck, sound like duck, walk like duck, swim like duck will be a duck
#the object of a class behaves like an object of another class(ie, have the same fun()), then it is duck typing
# class Animal:
#     def perform(self):
#         print("animal")
# class Human:
#     def perform(self):
#         print("human")
# class Circus:
#     def play(self,animal:Animal):
#         animal.perform()
# cat=Animal()
# navya=Human()
# c=Circus()
# c.play(cat)
# c.play(navya)


#class object as variable in another class
# class Company:
#     def __init__(self,name,loc,ceo):
#         self.cname=name
#         self.loc=loc
#         self.ceo=ceo
# class Employee:
#     def __init__(self,name,age,id,comp:Company): #here the comp is the object of another class company
#         self.name=name
#         self.age=age
#         self.id=id
#         self.company=comp
#     def disply(self):
#         print("name of emp:",self.name)
#         print("age of emp:", self.age)
#         print("name of company:", self.company.cname) #cant use comp or c, bcoz, we already set that self.company=comp
#         print("loc of comp:", self.company.loc)
# c=Company("nk bakes","calicut","nasrin")
# e1=Employee("ramya",20,101,c)
# e1.disply()