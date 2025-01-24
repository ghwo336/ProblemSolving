from collections import deque
n,m=map(int,input().split())
dap=[0 for _ in range(n+1)]
graph=[[] for _ in range(n+1)]
valid=set()
for x in range(m):
    a,b=map(int,input().split())
    if (a,b) not in valid:
        graph[b].append(a)
        valid.add((a,b))
for x in range(1,n+1):
    un=1
    visit=set()
    q=deque()
    q.append(x)
    visit.add(x)
    while q:
        now=q.popleft()
        for u in graph[now]:
            if u not in visit:
                q.append(u)
                un+=1 
                visit.add(u)
    dap[x]=un
fiv=max(dap)
dapli=[]
for x in range(1,n+1):
    if dap[x]==fiv:
       dapli.append(x)
print(*dapli)
    
    