def combination(p):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (i!=j and j!=k and i!=k):

                     print(p[i], p[j], p[k])

b=[]
n= int(input("Enter no. of terms: "))
if(n>=4):
    print("Invalid")
    n=int(input("Enter three digit terms only "))
for v in range(0,n):
    m=int(input("Enter a term :"))
    b.append(m)

print(combination(b))
