"""prints the multiplication table of a number from 1 to 10"""

"""
num=int(input('Enter a number '))
mul=1
for i in range(1,11):
    mul=num*i
    print(i,' * ',num,' = ',mul)
"""
num=int(input('Enter a number '))
inter=int(input("Enter a range "))
mul=1
for i in range(1,inter+1):
    mul=num*i
    print(i,' * ',num,' = ',mul)