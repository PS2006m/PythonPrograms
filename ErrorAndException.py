print("Start Code")
try:
    a=int(input("Enter A : "))
    b=int(input("Enter B : "))
    c=a/b
    print("Division : ",c)
    l=[1,2,3,4,5]
    index=int(input("Enter index Number : "))
    print(l[index])
except ZeroDivisionError as e:
    print("Exception caught : ",e)
except ValueError as e:
    print("Exception caugth : ",e)
except IndexError as e:
    print("Exception caugth : ",e)
except Exception as e:
    print("Exception Caught : ",e)
#except ValueError as e:
 #   print("Exception caugth : ",e), this is allowed but wont matter as exception class is abov it 


print("End Code")
