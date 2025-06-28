"""
f=open("student.txt","r")
read=f.read() #also we can use readline() and readlines()
#when we use readline, it reads the firstline only. if we want to read the second line, then we want to call it again
#print(f.readline())
#print(f.readline())
#when we use readlines(), then it prints all the lines and prints them like a list
#print(f.readlines())
print(read)
f.close()
"""

#appending
# f=open("student.txt","a")
# f.write("Prathyudaya\nNiya therese\nMohammed hashil")
# f.close()

#count number of lines
# f=open("student.txt","r")
# length=len(f.readlines())
# print(length)

#another method for counting lines
# lines=sum(1 for each in open("student.txt")) #using comprehension
# print(lines)