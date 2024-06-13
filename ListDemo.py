l=[1,2,1.1,2.2,"tops",True,1,2,"python",10,20]

print(l)
l.append(100)#adds to last of string , can pass only one argument
print(l)
#l.clear()
#print(l)
l1=l.copy()
print(l1)
print(l.count(1))#here ans will be 3 instead of 2 as Mathematically true is taken as 1 and false is taken as 0
print(l.count(2))
l2=[1000,2000,3000]
l.extend(l2)#can add only list
print(l)
print(l.index(1.1))#prints index of 1.1
l.insert(5,101)#inserts 101 at 5 index and pushes the rest rightwards
print(l)
l.pop()#pops last element in list
print(l)
l.pop(5)#removes element at 5th index
print(l)
l.reverse()#reverses the list
print(l)
l3=[9,1,8,2,7]
l3.sort()#sorts the elemnents in ascending order, but of same datatype(although int and float can be sorted together),can write reverse=True in argument for descending order
print(l3)
l4=["Ronit","Dixit","Pratham","Ansh","Vishwa","Abhishek"]
l4.sort()
print(l4)
