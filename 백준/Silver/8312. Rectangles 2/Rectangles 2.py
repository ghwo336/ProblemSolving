n,m,p=map(int,input().split())
dap=0
for x in range(1,n+1):
    for y in range(1,m+1):
        if (x+y)*2>=p:
            dap+=(n-x+1)*(m-y+1)
print(dap)