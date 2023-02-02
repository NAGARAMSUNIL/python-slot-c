def gettotalnumberofsequences(m,n):
    if m<n:
        return 0
    if n==0:
        return 1
    res= gettotalnumberofsequences(m-1,n)+gettotalnumberofsequences(m//2,n-1)
    return res
if __name__=='__main__':
    m=10
    n=4
    print('total number of possible sequences:',gettotalnumberofsequences(m,n))
