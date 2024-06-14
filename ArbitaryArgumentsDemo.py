def test(a,b,c,*d,**e): #here *d creates a tupple and **e creates a dictionary
    print("A : ",a,"B : ",b,"C : ",c,"D : ",d,"E :",e)

test(1,2,3,409,55,666,76,x=20,y=42,z=0)

