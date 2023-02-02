num1=float(input("enter the first number"))
num2=float(input("enter the second number"))

print("press 1 for + \npress 2 for - \npress 3 for * \npress 4 for /")

choice=int(input("select the choice from 1-4"))

if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    print(num1/num2)
else:
    print("invalid number")
