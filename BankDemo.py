import random
class Bank:
    totalamount=0
    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        acno=str(acno)
        file.write("You created an account by account number "+acno)
        file.write("\n")
        print("You succesfully opened an account")
        print("*********************************************************")

    def deposit(self,amount):
        self.balance+=amount
        print("You succesfully deposited ",amount," Rs")
        print("*********************************************************")
        amount=str(amount)
        file.write("You deposited an amount of "+amount+" Rs")
        file.write("\n")

    def withdraw(self,amount,wcount,totalamount):
        if amount<=self.balance:
            totalamount+=amount
            if wcount<3 and totalamount<=50000 and amount<=50000:
                self.balance-=amount
                print("You succesfully withdrew an amount of ",amount," Rs")
                amount=str(amount)
                wcount+=wcount
                file.write("You withdrew an amount of "+amount+" Rs")
                file.write("\n")
                print("*********************************************************")
                return True
            else:
                if wcount>=3:
                    print("You reached max withdrawal capacity")
                    print("*********************************************************")
                    file.write("You reached max withdrawal capacity")
                    file.write("\n")
                else:
                    print("Can't withdraw more than 50000 overall")
                    print("*********************************************************")
                    file.write("You tried to withdraw a total of more than 50000")
                    file.write("\n")
        else:
            print("You need ",amount-self.balance," more Rs")
            amount=str(amount)
            file.write("You tried to withdraw an impossible amount of "+amount+" Rs")
            file.write("\n")

    def checkBalance(self):
        print("Your balance is ",self.balance)
        print("*********************************************************")
        file.write("You checked your balance")
        file.write("\n")

b1=Bank()
acno=random.randint(100000,999999)
print("Acno is ",acno)
acno=str(acno)
file=open(acno+".txt","w")
cname=input("Enter your name ")
balance=int(input("Enter your balance "))
b1.openAccount(acno,cname,balance)
wcount=0
while True:
    print("*********************************************************")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check balance")
    print("4.Exit")
    print("*********************************************************")
    choice=int(input("Enter your choice "))
    if choice==1:
        amount=int(input("Enter amount you want to deposit "))
        b1.deposit(amount)
        print("*********************************************************")
    elif choice==2:
        amount=int(input("Enter amount you want to withdraw "))
        flag=b1.withdraw(amount,wcount,b1.totalamount)
        if flag:
            wcount+=1
            b1.totalamount+=amount
        print("*********************************************************")
    elif choice==3:
        b1.checkBalance()
        print("*********************************************************")
    elif choice==4:
        print("Thank you for choosing us ")
        file.write("You exited our system")
        file.close()
        print("*********************************************************")
        file=open(acno+".txt","r")
        print(file.read())
        file.close()
        break
    else:
        print("Wrong choice , Enter between 1 and 4")
