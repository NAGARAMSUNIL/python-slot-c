def hapnum(num):
    x=sum=0;
    if(num<0):
        print("doesnot exist")
    while(num>0):
        x=num%10;
        sum=sum+(x*x);
        num=num//10;
    return sum;
num=int(input("enter the number:"))
result=num;
while(result!=1 and result!=4):
    result=hapnum(result);
if(result==1):
    print(str(num)+"is a happy number");
elif(result==4):
    print(str(num)+"is not a happy number");
    
