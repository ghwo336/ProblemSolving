n,m,k=map(int,input().split())
li=[0 for _ in range(n+1)]
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
for x in li1:
    li[x]=1
for x in li2:
    li[x]=1
dap=[]
for x in range(1,n+1):
    if not li[x]:
        dap.append(x)
print(len(dap))
print(*dap)