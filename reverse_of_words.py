my_str=input('Enter a string ')
my_list=my_str.split(' ')
print(my_str)
for element in my_list:
    rev=element[::-1]
    print(rev,end=" ")