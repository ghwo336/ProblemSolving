from collections import deque
n,m=map(int,input().split())
dapLi=[10000000 for _ in range(n+1)]
visit=set()
graph=[[] for _ in range(n+1)]
for x in range(m):
    a,b=map(int,input().split())
    if (a,b) not in visit:
        visit.add((a,b))
        visit.add((b,a))
        graph[a].append(b)
        graph[b].append(a)

for x in range(1,n+1):
    start=x
    dp=[50000 for _ in range(n+1)]
    dp[start]=0
    q=deque()
    q.append((start,0))
    while q:
        now,num=q.popleft()
        for y in graph[now]:
            if dp[y]==50000:
                dp[y]=num+1
                q.append((y,num+1))
    dapLi[x]=sum(dp)-50000

fiv=min(dapLi)

for x in range(1,n+1):
    if dapLi[x]==fiv:
        print(x)
        break
                
    