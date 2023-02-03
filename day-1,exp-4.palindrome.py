def ispalindrome(x):
    return x==x[::-1]
x=str(input("enter the string:"))
ans=ispalindrome(x)
if ans:
    print("true")
else:
    print("false")
    
