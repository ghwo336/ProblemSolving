n,m=map(int,input().split())
inf = 10**13
li=list(map(int,input().split()))
dap=0
for x in range(1,n):
    if abs(li[x-1]-li[x])<m:
        li[x]=inf
        dap+=1
print(dap)