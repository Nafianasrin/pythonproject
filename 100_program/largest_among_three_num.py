num1=int(input('Enter 3 numbers '))
num2=int(input())
num3=int(input())
if num1>num2:
    if num1>num3:
        print('Largest is',num1)
    else:
        print('Largest is ',num3)
else:
    if num2>num3:
        print('Largest is ',num2)
    else:
        print('Largest is ',num3)