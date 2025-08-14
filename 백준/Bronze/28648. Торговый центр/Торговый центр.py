t=int(input())
dap=10000000000000000000000000
for x in range(t):
    a,b=map(int,input().split())
    dap=min(dap,a+b)
print(dap)