n=int(input())
li=list(map(int,input().split()))
dap=0
for x in range(n):
    hubo=0
    minfiv=-10000000000000000
    for y in range(x+1,n):
        if (li[y]-li[x])/(y-x)>minfiv:
            hubo+=1
            minfiv=(li[y]-li[x])/(y-x)
    maxfiv=100000000000000000
    for y in range(x):
        k=x-y-1
        if (li[x]-li[k])/(x-k)<maxfiv:

            hubo+=1
            maxfiv=(li[x]-li[k])/(x-k)

    dap=max(dap,hubo)

    
print(dap)
        
        
        