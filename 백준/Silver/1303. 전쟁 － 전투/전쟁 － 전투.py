from collections import deque

n,m=map(int,input().split())
graph=[list(input()) for _ in range(m)]
dap1=0
dap2=0
dx=[0,0,1,-1]
dy=[1,-1,0,0]
# dap1 계산
visit=[[False for _ in range(n)] for _ in range(m)]
for y in range(m):
    for x in range(n):
        dap=0
        if not visit[y][x] and graph[y][x]=='W':
            dap+=1
            visit[y][x]=True
            q=deque()
            q.append((x,y))
            while q:
                nowx,nowy=q.popleft()
                for i in range(4):
                    px=nowx+dx[i]
                    py=nowy+dy[i]
                    if 0<=px<n and 0<=py<m:
                        if not visit[py][px] and graph[py][px]=='W':
                            dap+=1
                            q.append((px,py))
                            visit[py][px]=True
        dap1+=dap**2



visit=[[False for _ in range(n)] for _ in range(m)]
for y in range(m):
    for x in range(n):
        dap=0
        if not visit[y][x] and graph[y][x]=='B':
            dap+=1
            visit[y][x]=True
            q=deque()
            q.append((x,y))
            while q:
                nowx,nowy=q.popleft()
                for i in range(4):
                    px=nowx+dx[i]
                    py=nowy+dy[i]
                    if 0<=px<n and 0<=py<m:
                        if not visit[py][px] and graph[py][px]=='B':
                            dap+=1
                            q.append((px,py))
                            visit[py][px]=True
        dap2+=dap**2


print(dap1,dap2)
