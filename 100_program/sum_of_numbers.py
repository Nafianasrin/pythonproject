#sum of n natural numbers
"""
num=int(input("Enter a number "))
sums=0
for i in range(num+1):
    sums=sums+i
print("The sum of ",num," numbers is ",sums)
"""
num=int(input("Enter a number "))
print("The sum of ",num," numbers is ",int((num*(num+1))/2))