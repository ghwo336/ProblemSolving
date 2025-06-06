n=int(input())
while(n!=1):
    for x in range(2,n+1):
        if (n%x==0):
            print(x)
            n//=x
            break
            