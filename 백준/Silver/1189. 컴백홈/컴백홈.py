def dfs(tx,ty,num):
    global dap
    if num==k and tx==0 and ty==m-1:
        dap+=1
        return
    for i in range(4):
        px=tx+dx[i]
        py=ty+dy[i]
        if 0<=px<n and 0<=py<m and not visit[px][py]:
            if graph[px][py]!='T':
                visit[px][py]=True
                dfs(px,py,num+1)
                visit[px][py]=False

n,m,k=map(int,input().split())
graph=[list(input()) for _ in range(n)]
visit=[[False for _ in range(m)] for _ in range(n)]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
dap=0
if graph[n-1][0]=='T':
    print(0)
else:
    visit[n-1][0]=True
    dfs(n-1,0,1) 
    print(dap)