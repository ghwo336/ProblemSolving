p,m,c=map(int,input().split())
x=int(input())
dap=1000000000000000000
for i in range(1,p+1):
    for j in range(1,c+1):
        for k in range(1,m+1):
            dap=min(dap,abs((i+k)*(k+j)-x))
print(dap)