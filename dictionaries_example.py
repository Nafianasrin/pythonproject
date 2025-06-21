#a dictionary can also contain a list
sample={'name':'nafia','age':21,'colors':['red','blue']}
print(sample)
print(len(sample))
print(type(sample))

#getting the value of a key
print(sample['name'])
x=sample.get('name')
print(x)

#another way to create dict
person=dict(name='john',age=36)
print(person)

#getting all keys and values
y=sample.values() #whether you can use a variable like this
print(y) #or
print(sample.keys()) #you can simply print like this

#to get each element in a dict as tuples
tup=sample.items()
print(tup)

#check whether a key is in dict
if 'age' in sample:
    print('yes',sample['age'])

#changing values
sample['age']=24 #1st method
print(sample)
sample.update({'age':26}) #2nd method
print(sample)

#adding items
sample['address']='calicut' #1st method
print(sample)
sample.update({'year':2025}) #2nd method
print(sample)

#removing items
sample.pop('year') #removes the key named year
print(sample)
sample.popitem() #removes the last item
print(sample)
del sample['colors'] #removes the key colors
print(sample)
"""
sample.clear() #empties the dict
print(sample)
del person #deletes the dict person
print(person)
"""

#loop
for x in sample: #prints the keys in the dict 1st method
    print(x,end=" ")
print('\n')
for x in sample.keys(): #2nd method
    print(x)
for x in sample: #prints the values 1st method
    print(sample[x])
for x in sample.values(): #2nd method
    print(x)
for x,y in sample.items(): #prints elements
    print(x,y)