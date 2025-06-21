"""
Accept the mark list of a student for 5 subjects.
calculate the total, average and grade and display the final result.
"""
mark_list=[]
total=0
for i in range(0,5):
    element=int(input('Enter the mark(Max mark is 100)'))
    mark_list.append(element)
print(mark_list)
for num in mark_list:
    total+=num
print('Total mark obtained is ',total)
print('Average mark is ',total/5)
if total>450:
    print('Grade is A')
elif total>400:
    print('Grade is B')
elif total>350:
    print('Grade is C')
elif total>300:
    print('Grade is D')
elif total>250:
    print('Grade is E')
else:
    print('You have failed!')