"""
print all prime numbers in an intervel
"""
inter=int(input("Enter an intervel "))
print("2",end=" ")
for num in range(2,inter):
    flag=0
    for i in range(2,num):
        if num%i == 0:
            flag=0
            break
        else:
            flag=1
    if flag==1:
        print(num, end=" ")
