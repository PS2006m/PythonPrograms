file=open("tops1.txt","w")
s="This is file write operation using python ."
file.write(s)
file.close()
print("File Written Succesfully ")
print("******************************************")

file=open("tops1.txt","r")
print(file.read())
file.close()
print("************************************")

file=open("tops1.txt","a")
file.write("\nThis file is now appended")
file.close()
print("******************************")

file=open("tops2.txt","w+")
file.write("This file is w+ using python")
print("Current Position : ",file.tell())#tell gives the current position of cursor
file.seek(0)#seek sets the cursor to whatver argument is passed inside
print(file.read())
file.close()
print("************************************")
