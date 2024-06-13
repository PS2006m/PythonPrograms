import random

print(random.randint(1,100))
print(random.choice([1,2,3,"tops","java",100,232.2]))#choice only for list

l=[]
lucky=[]

for i in range(1,101):
    l.append(i)

for i in range(1,11):
    a=random.choice(l)
    l.remove(a)
    lucky.append(a)
print(l)
print(lucky)

