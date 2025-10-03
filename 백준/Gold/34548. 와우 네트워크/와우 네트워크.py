import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
li=[]
parents=list(range(n+1))

def find(x):
    if x==parents[x]:
        return x
    else:
        parents[x]=find(parents[x])
    return parents[x]
def union(x,y):
    rootX=find(x)
    rootY=find(y)
    if rootX==rootY:
        return
    parents[max(rootX,rootY)]=min(rootX,rootY)



for x in range(m):
    start,end,time=map(int,input().split())
    li.append([time,start,end])
li.sort()
dap=0
nowt=1
for x in li:
    dap+=(n*(x[0]-nowt))
    if find(x[1])!=find(x[2]):
        n-=1
        union(x[1],x[2])
    nowt=x[0]
dap+=n*(k-nowt+1)
print(dap)
    