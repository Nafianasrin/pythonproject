#print the armstrong numbers in an intervel

upper=int(input("Enter the upper limit "))
for num in range(upper):
    n=0
    sums=0
    for digit in str(num):
        n+=1
    for i in str(num):
        sums=sums+(int(i)**n)
    if num==sums:
        print(num,end=" ")
    else:
        continue