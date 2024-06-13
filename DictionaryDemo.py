d={123:"Vansh",456:"Pratham",567:"Shivam",678:"Rishil",876:"Vishal"}
print(d)
print(d.get(456))
print(d.items())
print(d.keys())
print(d.values())
d.pop(678)
print(d)
d.popitem()
print(d)
d1={110:"Rishil",111:"Vishal",123:"Tirth"}
d.update(d1)
print(d)

for i in d:
    print(i)
