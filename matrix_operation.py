"""add,multiply, substract two matrices from the user """


import numpy as np
x=np.array([[2,3,1],[4,5,6],[7,8,9]])
det_x = np.linalg.det(x)
print("Determinant:", det_x) #if it is zero, it is singular
#x=np.arange(1,10)
#x=np.zeros((3,3))
#x=np.ones((3,3))
# print(x)
# print(x[1]) #to print a particular row
# #print(x[:0]) #to print a particular column??????
# print(x.shape) #to get the size of matrix
y=np.array([[1,2,3],[2,3,4],[3,4,5]])
a=x+y
b=x+5
c=x*5
d=x-y
e=np.dot(x,y)
f=x.T
g=np.linalg.inv(x) # linalg represents linear algebra which a subprogram in numpy
h=np.linalg.inv(f) #gives inverse it it is not a singular matrix
i=np.linalg.matrix_rank(x) #to find the rank of the matrix
j=np.linalg.eig(x)[0] #to find the eigen values of matrix
k=np.linalg.pinv(y) #it will give the inverse of any matrix whether it is singular or not
print("addition",a)
print("scalar addition",b)
print("scalar multiplication",c)
print("subtraction",d)
print("multiplication",e)
print("transpose",f)
print("inverse",g)
print("by inversing an inversed matrix we will get the original matrix",h)
print("rank",i)
print("eigan values",j)
print("inverse of y",k)