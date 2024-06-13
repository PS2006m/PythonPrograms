#capital letters , small letters , space , alphabets, numerical
s=input("Enter a String : ")
print("String is ")
print(s)

count=0
scount=0
acount=0
ncount=0
lcount=0
for i in s:
    if i.isupper():
        count=count+1
    if i.islower():
        scount=scount+1
    if i.isalpha():
        acount=acount+1
    if i.isnumeric():
        ncount=ncount+1
    if i.isspace():
        lcount=lcount+1
print("Capital letters ",count)
print("Small letters are ",scount)
print("Alphabets are ",acount)
print("Numbers are ",ncount)
print("Space is ",lcount)
