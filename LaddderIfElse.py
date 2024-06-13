rno=int(input("Enter Roll number "))
sname=input("Enter Name ")
s1=int(input("Enter marks of Subject 1 "))
s2=int(input("Enter marks of Subject 2 "))
s3=int(input("Enter marks of Subject 3 "))

total=s1+s2+s3
per=total/3

print("Roll no is ",rno)
print("Name is ",sname)
print("Total is ",total)
print("Percentage is ",per)

if per>=70:
    print("Distinction")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second Class")
elif per>=40:
    print("Pass Class")
else:
    print("Fail")
