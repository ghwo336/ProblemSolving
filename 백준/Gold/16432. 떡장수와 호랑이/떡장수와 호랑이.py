graph=[[]]
n=int(input())
for x in range(n):
    li=list(map(int,input().split()))
    li2=[]
    for y in range(li[0]):
        li2.append(li[y+1])
    graph.append(li2)

dp=[0 for _ in range(n+1)]
visit=[[False for _ in range(11)] for _ in range(n+2)]

def dfs(i):    
    global n
    if dp[n]!=0:
        return
    for x in graph[i]:
        if dp[n]!=0:
            return
        if dp[i-1]!=x:
            dp[i]=x
            if not visit[i+1][x]:
                visit[i+1][x]=True
                dfs(i+1)
dfs(1)

if dp[n]!=0:
    for x in range(1,n+1):
        print(dp[x])
else:
    print(-1)
    

        
        
    