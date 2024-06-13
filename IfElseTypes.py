'''
1. Simple If

    if condition:
        statement #The space left below if is called indentation

2.If-Else

    if condition:
        statement
    else:
        statement

3.Nested If

    if condition:
        if condition:
            statement
        else:
            statement
    else:
        statement

4.Ladder If

    if condition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    else:
        statement
'''
a=int(input("Enter A : "))
if a>0:
    print("A is Positive")
else:
    print("A is Negative")

if a%2==0:
    print("A is Even")
else:
    print("A is odd")

b=int(input("Enter B : "))
if a>b:
    print("A is Max Value")
else:
    print("B is Max Value")
    
