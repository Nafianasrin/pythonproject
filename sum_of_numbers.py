"""sum of n natural numbers"""
n=int(input('Enter a number '))
sum=0
for i in range(n+1):
    sum+=i
print('The sum of ',n,' natural numbers is ',sum)