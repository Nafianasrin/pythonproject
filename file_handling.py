f=open("student.txt","w") #this txt will be created at the same location of the python file file_handling
#if we want that file in a specified location, then the path should be specified like this
#f=open("F:/Downloads/File/student.txt","w")
#if we want a word file, then docx instead of txt.
#f.write("Natha azeez\nNafia nasrin") mainly for writing a string
f.writelines(["Natha azeez\n","Nafia nasrin\n","Hamda fathima\n","Shan raj\n","Amith\n"]) #using list
f.close()