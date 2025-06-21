print('hi, welcome to engineers squad')
'''mylist=[1,2,3,4,1,3,5,6,2]
myset=set(mylist)
print(list(myset))'''
'''mylist=[1,2,3,4,1,3,5,6,2]
newlist=[]
for x in mylist:
    if mylist[x] not in newlist:
        newlist.append(mylist[x])
print(newlist)'''
list1=[1,2,3,4,1,3,5,6,2,7]
list2=list()
for x in list1:
    if x not in list2:
        list2.append(x)
print(list2)