#it prints 0,1,1,2,3,5,8,13,21,34,55,89,144,....
"""
n=int(input("Enter a number "))
sum=[0,1]
for i in range(n):
    sum.append(sum[-1]+sum[-2])
print(sum)
"""
terms=int(input("Enter how many terms you needed "))
n1,n2=0,1
if terms<0:
    print("Enter a positive one ")
elif terms==1:
    print(n1)
elif terms==2:
    print(n1,n2)
else:
    print(n1,n2,end=" ")
    for i in range(2,terms+1):
        s=n1+n2
        print(s,end=" ")
        n1,n2=n2,s


