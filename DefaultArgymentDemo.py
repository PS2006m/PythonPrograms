def test(a,b,c,d=10): #Value given to d is called default argument
    print("A : ",a,"B : ",b,"C : ",c,"D : ",d)

test(1,2,3)#its optional to pass value for d , is passed it will overwrite 10

def test(a=40,b=30,c=20,d=10): 
    print("A : ",a,"B : ",b,"C : ",c,"D : ",d)

test(b=100,c=400)#this is called keyword argument, will overwrite b and c
