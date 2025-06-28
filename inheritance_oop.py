class person:
    def __init__(self):
        print("this is parent class")

    def display(self,name,age):
        print("name : ",name)
        print("age : ",age)

class student(person):
    def __init__(self):
        print("this is child class")

    def sdisplay(self,sname,sage,sid):
        print("name : ",sname)
        print("age : ", sage)
        print("ID id : ",sid)

std1=student()
std1.sdisplay("ramya",18,1)
std1.display("manav",34)
a=person()
