lim=int(input("enter the limit"))
num=int(input("enter the number"))
count=0
for i in range(1,lim+1):
    if i % num==0:
        print(i)
        count+=1
if count==0:
    print("no such numbers")
else:
    print("the numbers that are divisible by ", num, "within the limit are given above ","\u261D\uFE0F"*4)
print("\U0001F602"*20)