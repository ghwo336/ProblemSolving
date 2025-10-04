#24391
import sys
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
li3=list(map(int,input().split()))
now=li3[0]
dap=0
for x in range(len(li3)-1):
    if find(now)!=find(li3[x+1]):
        now=li3[x+1]
        dap+=1
print(dap)