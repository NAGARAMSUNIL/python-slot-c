s = input("enter the string:")
l,u = 0,0
for i in s:
    if (i>='a'and i<='z'):
    
        l=l+1               
    if (i>='A'and i<='Z'):
         
        u=u+1
         
print('number of small letters: ',l)
print('numbers 0f caps: ',u)
