import sys
sys.setrecursionlimit(10**9)
def dfs(x,y):
    if x==m-1 and y==n-1:
        return 1
    if visit[y][x]!=-1:
        return visit[y][x]
    visit[y][x]=0
    for k in range(4):
        ny=y+movey[k]
        nx=x+movex[k]
        if 0<=nx<m and 0<=ny<n:
            if graph[y][x]>graph[ny][nx]:
                visit[y][x]+=dfs(nx,ny)
    return visit[y][x]
n,m=map(int,input().split())
graph=[]
movex=[0,-1,1,0]
movey=[1,0,0,-1]
for x in range(n):
    li=list(map(int,input().split()))
    graph.append(li)
visit=[[-1 for _ in range(m)] for _ in range(n)]
print(dfs(0,0))



