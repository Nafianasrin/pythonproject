my_list=[5,4,7,10,8,2]
length=len(my_list)
a=int(input('enter the index '))
if a<length:
    list1=my_list[a: ]+my_list[ :a]
    print(list1)
else:
    print('index you entered is out of range')

"""
out1:-
enter the index 8
index you entered is out of range

out2:-
enter the index 2
[7, 10, 8, 2, 5, 4]

"""