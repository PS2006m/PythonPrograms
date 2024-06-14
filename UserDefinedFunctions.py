'''
Function is a set of instructions that perform a specific task
'''
def printLine(): #def key word is used to  define a function
    print("*"*50)

printLine()
print("This is a user defined function")
printLine()

def add(a,b):
    print("Addition : ",a+b)

printLine()
add(10,20)
print(add(10,20))#function will be called but as no return type , here None will printed
printLine()

def sub(a,b):
    return a-b

printLine()
ans=sub(10,20)
print("Subtraction : ",ans)
# or can also do directly by calling in print
print("Subtraction : ",sub(10,20))
printLine()
