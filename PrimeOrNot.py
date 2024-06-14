def prime(n):
    if n==2 or n==1:
        print("It is a prime number")
        return
    if n%2==0:
        print("Not a Prime Number")
    else:
        for i in range(3,int(n/2)+1,+2):
            if n%i==0:
                print("Not a Prime Number")
                break
        else:
             print("It is a Prime Number")


a=int(input("Enter number : "))
prime(a)
            
                
            
