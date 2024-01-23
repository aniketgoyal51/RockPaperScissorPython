import random

choose=[1,2,3]
print("1. Scissor\n2. Rock\n3. Paper ")
user=int(input("What is your choice: "))
if user < 1 or user > 3:
    print("Invalid Choice")
else:
    comp=random.randint(1,len(choose))
    print("Comp action is:", comp)
    if(comp==user):
        print("Draw")
    elif(comp==1 or user==3) or (comp==2 and user==1) or(comp==3 and user==2):
        print("Comp Won")
    else:
        print("User Won")
  