a,b,c=map(int,input().split())
dap=-1
for x in range(c+1):
    m=a-x
    g=b-(c-x)
    dap=max(dap,min(m//2,g))
print(dap)
    