# m=lambda : print("helloworld")
# m() #lambda arguments:expression
"""
t=int(input("enter the number of terms"))
for i in range(t):
    power=2**i
    print("2 **",i," is ",power)
"""
t=int(input("enter the number of terms"))
result=list(map(lambda x:2 **x, range(t)))
for i in range(t):
    print("2 **", i, " is ", result[i])