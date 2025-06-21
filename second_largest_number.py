num_list=[]
n=int(input('Enter the length of the list '))
for i in range(0,n):
    num=int(input('Enter the numbers in the list\n'))
    num_list.append(num)
print(num_list)
new_list=sorted(num_list)
print('The second largest element is ',new_list[-2])