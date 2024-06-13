import random
num=int(input("Enter a number between 1 and 20 : "))
l=[]
for i in range(1,21):
    l.append(i)
a=random.choice(l)

while True:
    if a==num:
        print("You guessed correctly")
        break
    elif num>a:
        print("Your guess is higher than the number")
        num=int(input("Enter again : "))
    elif num<a:
         print("Your guess is lesser than the number")
         num=int(input("Enter again : "))
    else:
        num=int(input("Enter a number between 1 and 20 :"))
