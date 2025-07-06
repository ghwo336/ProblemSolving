from collections import deque
inf=200000000
n=int(input())
graph=[[0 for _ in range(501)] for _ in range(501)]
dp=[[inf for _ in range(501)] for _ in range(501)]
for _ in range(n):
    x1,y1,x2,y2=map(int,input().split())
    for x in range(min(x1,x2),max(x1,x2)+1):
        for y in range(min(y1,y2),max(y1,y2)+1):
            graph[x][y]=1
m=int(input())
for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    for x in range(min(x1,x2),max(x1,x2)+1):
        for y in range(min(y1,y2),max(y1,y2)+1):
            graph[x][y]=inf
graph[0][0]=0
dp[0][0]=0
q=deque()
q.append((0,0))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
while q:
    nowx,nowy=q.popleft()
    for i in range(4):
        if 0<=nowx+dx[i]<=500 and 0<=nowy+dy[i]<=500:
            if dp[nowx+dx[i]][nowy+dy[i]]>dp[nowx][nowy]+graph[nowx+dx[i]][nowy+dy[i]]:
                dp[nowx+dx[i]][nowy+dy[i]]= dp[nowx][nowy]+graph[nowx+dx[i]][nowy+dy[i]]
                q.append((nowx+dx[i],nowy+dy[i]))
if dp[-1][-1]!=inf:
    print(dp[-1][-1])
else:
    print(-1)
        
        
