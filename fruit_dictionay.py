"""
takes a string of fruits and count the occurences of each fruit.
print dictionary as fruit as key and occurences as value.
"""
fruits=input('Enter the fruits name ')
fruit=list(fruits.split(' '))
list1=[]
for i in range(0,len(fruit)):
    count=1
    for j in range(0,i):
        if fruit[i] == fruit[j]:
            count=count+1
    list1.append(count)
#print(fruit)
#print(list1)
#s_dict={}
#for x in range(len(fruit)):
#    if x<len(list1):
#        s_dict[fruit[x]]=list1[x]
#print(s_dict)
my_dict=dict(zip(fruit,list1))
print(my_dict)
