#24391
import sys
import heapq
input=sys.stdin.readline
n,m=map(int,input().split())
parents=[x for x in range(n+1)]
def find(x):
    if x==parents[x]:
        return x
    parents[x]=find(parents[x])
    return parents[x]

def union(x,y):
    parentx=find(x)
    parenty=find(y)
    if parentx==parenty:
        return
    parents[max(parentx,parenty)]=min(parentx,parenty)
    return

li=[]
for _ in range(m):
    li2=list(map(int,input().split()))
    li.append(li2)
li.sort()

for x in li:
    union(x[0],x[1])
for x in range(n+1):
    find(x)
c,h,k=map(int,input().split())
no=find(h)
now=find(c)
di=dict()
for x in range(1,n+1):
    p=find(x)
    if p not in di:
        di[p]=1
    else:
        di[p]+=1
di.pop(no)
dap=di[now]
di.pop(now)
heap=[]
for x in di:
    heapq.heappush(heap,-di[x])
for i in range(k):
    if heap:
        dap-=heapq.heappop(heap)
    else:
        break
print(dap)
        
