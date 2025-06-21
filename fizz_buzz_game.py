"""
print from 1 to 50. If a number divisible by 3, print fizz
if a number is divisible by 5,print buzz.
If a number divisible by both 3 and 5, print fizzbuzz
"""
n=int(input('Enter the limit '))
for i in range(n+1):
    if i%3==0 and i%5==0:
        print(i,"  FizzBuzz")
    elif i%3==0:
        print(i,"  Fizz")
    elif i%5==0:
        print(i,"  Buzz")
    else:
        print(i)