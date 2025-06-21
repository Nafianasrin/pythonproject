# m=int(input("enter the number of rows"))
# n=int(input("enter the number of columns"))
# p=int(input("enter the number of rows"))
# q=int(input("enter the number of columns"))
# if m!=p or n!=q:
#     print("addition is not possible")
# else:
#     m1=[]
#     print("enter your first matrix")
#     for i in range(m):
#         a=[]
#         for j in range(n):
#             a.append(int(input()))
#         m1.append(a)
#     m2 = []
#     print("enter your second matrix")
#     for i in range(p):
#         a = []
#         for j in range(q):
#             a.append(int(input()))
#         m2.append(a)
#     print("first matrix")
#     for i in range(m):
#         for j in range(n):
#             print(m1[i][j],end=" ")
#         print()
#     print("second matrix")
#     for i in range(p):
#         for j in range(q):
#             print(m2[i][j], end=" ")
#         print()
#     print("addition matrix")
#     for i in range(m):
#         for j in range(n):
#             print(m1[i][j]+m2[i][j], end=" ")
#         print()

"""add,multiply, subtract two matrices from the user """

import numpy as np
m=int(input("enter the number of rows of first matrix "))
n=int(input("enter the number of columns of first matrix "))
m1=np.ndarray(shape=(m,n),dtype=int)
print("enter %d elements: "%(m*n))
for i in range(m):
    for j in range(n):
        m1[i][j]=int(input())

p=int(input("enter the number of rows of second matrix "))
q=int(input("enter the number of columns of second matrix "))
m2=np.ndarray(shape=(p,q),dtype=int)
print("enter %d elements: "%(p*q))
for i in range(p):
    for j in range(q):
        m2[i][j]=int(input())

print("first matrix is \n",m1)
print("second matrix is \n",m2)

def add(m1,m2):
    sum=m1+m2
    print('sum is \n',sum)
def sub(m1,m2):
    difference=m1-m2
    print('difference is \n', difference)
def mul(m1,m2):
    product=np.dot(m1,m2)
    print('product is \n', product)

def choices():
    print('select operation ')
    choice=int(input("1.Addition 2.Subtraction 3.Multiplication "))
    if choice==1:
        if m!=p or n!=q:
            print("Addition is not possible")
        else:
            add(m1,m2)
    elif choice==2:
        if m!=p or n!=q:
            print("subtraction is not possible")
        else:
            sub(m1,m2)
    elif choice==3:
        if n!=p:
            print("Multiplication is not possible")
        else:
            mul(m1,m2)
    else:
        print('invalid choice ')
        ch = int(input('do you want to continue '))
        if ch==1:
            choices()
choices()