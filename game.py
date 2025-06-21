
"""
num=[2,34,67,999,8,25,89,100]
print(sorted(num)[-1])
num_sort=sorted(num)
a=len(num_sort)-1
print(num_sort[a])"""
num=[]
n=int(input('enter the total number of elements in list'))
for i in range(0,n):
    elements=int(input('enter the number'))
    num.append(elements)
print(num)
#num=[2,34,67,8,25,89]
largest=num[0]
for number in num:
    if number > largest:
        largest=number
print(largest)

#print(num[0:4])
