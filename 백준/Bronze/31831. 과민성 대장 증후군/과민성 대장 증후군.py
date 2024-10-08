n,m=map(int,input().split())
li=[0]+list(map(int,input().split()))
for x in range(1,n+1):
    if li[x]+li[x-1]>=0:
        li[x]+=li[x-1]
    else:
        li[x]=0
dap=0
for x in li:
    if x>=m:
        dap+=1
print(dap)
