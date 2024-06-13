for i in range(1,10):
    print("*"*i)
print("---------------------------------")

for i in range(1,10):
    for j in range(i):
        print("*",end="")
    print("")
print("----------------------------------")

for i in range(1,10):
    print(" "*(9-i)+"*"*i)
print("------------------------------")

for i in range(1,10):
    print(" "*(9-i)+"*"*i+"*"*(i-1))
print("------------------------------")


for i in range(1,10):
    print(" "*(9-i)+" *"*i)
print("--------------------------------")

for i in range(9,0,-1):
    print(" "*(9-i)+"*"*i+"*"*(i-1))
