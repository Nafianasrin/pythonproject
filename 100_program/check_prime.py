num=int(input('Enter a number '))
flag=0
if num==0 | num==1:
    print('number is not a prime')
elif num==2:
    print('number is a prime')
else:
    for i in range(2,num):
        if num%i==0:
            flag=1
            break
    if flag==1:
        print(' prime')
    else:
        print('not prime')
