def dfs(x,y,value,op):
    global mindap,maxdap,n
    if x==n-1 and y==n-1:
        mindap=min(mindap,value)
        maxdap=max(maxdap,value)
        return
    for i in range(2):
        nowx=x+dx[i]
        nowy=y+dy[i]
        if 0<=nowx<n and 0<=nowy<n:
            if graph[nowx][nowy] in s:
                dfs(nowx,nowy,value,graph[nowx][nowy])
            else:
                if op=="+":
                    dfs(nowx,nowy,value+graph[nowx][nowy],"")
            
                elif op=="-":
                    dfs(nowx,nowy,value-graph[nowx][nowy],"")
                elif op =="*":
                    dfs(nowx,nowy,value*graph[nowx][nowy],"")
            
    
    
    


n=int(input())
mindap=100000000000000000
maxdap=-10000000000000000
graph=[]
s={"+","*","-"}
dx=[0,1]
dy=[1,0]
for x in range(n):
    li=list(input().split())
    graph.append(li)
for x in range(n):
    for y in range(n):
        if (x+y)%2==0:
            graph[x][y]=int(graph[x][y])
dfs(0,0,graph[0][0],"")

print(maxdap,mindap)