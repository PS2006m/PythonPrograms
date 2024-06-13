t=(1,2,3,1.1,2.2,"tops",[10,20,30],"java",1,True,34,True)

print(t)
print(t.count(True))
print(t.index(2.2))
for i in t:
    print(i)
print("java" in t)
print(t[6])
t[6].append(40)
print(t[6])
l=[1,2,3]
t1=tuple(l)
print(t1)
l1=list(t1)
print(l1)
t2=(l)#this will be just stored  as list
print(t2)
