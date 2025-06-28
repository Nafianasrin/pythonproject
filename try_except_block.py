#File not found errors(FileNotFoundError)
#Permission issues(PermissionError)
#Any other unexpected errors

try:
    f=open("student.txt","r")
    if x==5:
       print("x is 5") #name error occured since x is initialized
except FileNotFoundError:
    print("File not exist..!")
except NameError as e:
    print(e) #this will print what error is, instead of a custom message
except Exception as e:
    print(e)
else:
    print(".............") #only runs if there is no exceptions
finally:
    print("Always runs")

#raising exception by our own
# try:
#     f=open("teacher.txt","r")
#     if f.name=="teacher.txt":
#         raise Exception
# except Exception:
#     print("Error occured")