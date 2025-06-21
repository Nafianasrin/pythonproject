"""
Given two tuples. Program to create a dictionary such that keys from tup1 in reverse order and
values from tup2 in actual order.
Print the dictionary and second last values from dictionary.
"""


tup1=('1','2','3','4','5')
tup2=('apple','bat','car','dog')
rev=tuple(reversed(tup1))
s_dict={}
for x in range(len(rev)):
    # s_dict[rev[x]]=[tup2[i] for i in range(len(tup2)) if i==x]
    if x<len(tup2):
        s_dict[rev[x]]=tup2[x]
print(s_dict)
values=list(s_dict.values())
print('second last value is ',values[-2])


"""
tup1=('1','2','3','4','5')
tup2=('apple','bat','car','dog')
my_dict=dict(zip(reversed(tup1),tup2))
print(my_dict)
value=list(my_dict.values())
print(value[-2])
"""