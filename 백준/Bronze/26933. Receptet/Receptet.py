t=int(input())
dap=0
for x in range(t):
    a,b,c=map(int,input().split())
    dap+=max(b-a,0)*c
print(dap)