"""
define 4 functions, add sub div multiply.
should contain multiple times
exits when use choose 5
"""
def add(a,b):
    sum=a+b
    print('sum of ',a,' and ',b,' is ',sum)
def sub(a,b):
    difference=a-b
    print('difference of ', a, ' and ', b, ' is ', difference)
def mul(a,b):
    product=a*b
    print('product of ', a, ' and ', b, ' is ', product)
def div(a,b):
    if b!=0:
        division=a/b
        print(a,' divided by ', b, ' is ', division)
    else:
        print('division by zero is not possible')
#main program
num1=int(input('enter a number '))
num2=int(input('enter another one '))
def choices():
    print('select operation')
    choice=int(input("1.Addition 2.Substraction 3.Multiplication 4.Division 5.Exit "))
    if choice==1:
        add(num1,num2)
        ch = int(input('do you want to continue '))
        if ch==1:
            choices()
    elif choice==2:
        sub(num1,num2)
        ch = int(input('do you want to continue '))
        if ch==1:
            choices()
    elif choice==3:
        mul(num1,num2)
        ch = int(input('do you want to continue '))
        if ch==1:
            choices()
    elif choice==4:
        div(num1,num2)
        ch = int(input('do you want to continue '))
        if ch==1:
            choices()
    elif choice==5:
        return
    else:
        print('invalid choice ')
        ch = int(input('do you want to continue '))
        if ch==1:
            choices()
choices()
