
a=int(input('enter a number '))
b=int(input('enter another one '))
c = input('1.Addition 2.Difference 3.Product 4.Division 5.Floor division 6.Exponent 7.modulus ')

def choices():
    choice=int(c)
    match choice:
        case 1:
            print('the addition of two numbers is ',a + b)
        case 2:
            print('the subtraction of two numbers is ', a - b)
        case 3:
            print('the product of two numbers is ', a * b)
        case 4:
            print('the division of two numbers is ', a / b)
        case 5:
            print('the floor division of two numbers is', a // b)
        case 6:
            print('the result of a^b is ', a ** b)
        case 7:
            print('the remainder after dividing two numbers is ', a % b)
        case _:
            print('invalid selection')

choices()


'''a=int(input('enter a number '))
b=int(input('enter another one '))
c=input('enter a arithmetic operation(ie, +,-,*,/,//,%,**) ')
if c== '+':
     print(a, '+' ,b, '=',a+b)
elif c=='-':
     print(a, '-', b, '=', a - b)
elif c=='*':
     print(a, '*', b, '=', a * b)
elif c=='/':
    print(a, '/', b, '=', a / b)
elif c=='//':
    print(a, '//', b, '=', a // b)
elif c=='**':
    print(a, '**', b, '=', a ** b)
elif c=='%':
    print(a, '%', b, '=', a % b)
else:
    print('invalid sign')'''
