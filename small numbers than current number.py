n=[3,5,6,7,1,2,9,0]
lst()
for i in range(len(n)):
    count=0
    for j in range(0,len(n)):
        if (n[i]>n[j]):
            count=count+1
        else:
            continue
        lst.append(count)
    print(lst)
            
