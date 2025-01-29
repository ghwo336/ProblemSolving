n,m,k=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
visit=[[False for _ in range(m)] for _ in range(n)]
dap=-1000000000000
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def track(px,py,num,hap):
    global n,m,k,dap
    if num==k:
        dap=max(dap,hap)
        return;
    for x in range(n):
        for y in range(m):
            if visit[x][y]:
                continue
            fiv=True
            for i in range(4):
                if 0<=x+dx[i]<n and 0<=y+dy[i]<m:
                    if visit[x+dx[i]][y+dy[i]]:
                        fiv=False
            if fiv:
                visit[x][y]=True
                track(x,y,num+1,hap+graph[x][y])
                visit[x][y]=False


track(0,0,0,0)
print(dap)