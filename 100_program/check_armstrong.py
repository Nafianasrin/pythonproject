#153 is armstrong number. 1^3 + 5^3 + 3^3 = 153

"""
n=int(input("Enter th digits of the number "))
num=input("Enter a number ")
nums=[]
sum=0
for digit in num:
    nums.append(int(digit))
if n!=len(nums):
    print("Enter the number of digits correctly ")
    exit()
else:
    for i in nums:
        sum=sum+(i**n)
if int(num)==sum:
    print("The given number is armstrong")
else:
    print("The given number is not armstrong")
"""
num=input("Enter a number ")
n=0
sums=0
for digit in num:
    n+=1
for i in num:
        sums=sums+(int(i)**n)
if int(num)==sums:
    print("The given number is armstrong")
else:
    print("The given number is not armstrong")