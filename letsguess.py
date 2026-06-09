import random as ran
guess = ran.randint(1,10)
no=1
while True:
    num=int(input("enter the number: "))
    if num>guess:
        print("too high")
    elif num<guess:
        print("too low")
    else:
        print("you won")
        break
    no+=1
print(no)