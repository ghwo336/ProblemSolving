mod=998244353
dap=1
n=int(input())
li=list(map(int,input().split()))
for x in range(n):
    if li[x]!=x+1:
        dap*=(n-2)
    else:
        dap*=(n-1)
    dap%=mod
print(dap)