n,m=map(int,input().split())
graph=[[0 for _ in range(m+1)]]
dap=-1000001
for x in range(n):
    li=[0]+list(map(int,input().split()))
    graph.append(li)
hap=[[0 for _ in range(m+1)] for _ in range(n+1)]
dp=[[-10001 for _ in range(m+1)] for _ in range(n+1)]

for y in range(1,n+1):
    for x in range(1,m+1):
        hap[y][x]+=hap[y-1][x]+hap[y][x-1]-hap[y-1][x-1]+graph[y][x]

for y in range(1,n+1):
    for x in range(1,m+1):
        for z in range(y,n+1):
            for w in range(x,m+1):
                dp[y][x]=max(dp[y][x],hap[z][w]-hap[y-1][w]-hap[z][x-1]+hap[y-1][x-1])


for y in range(1,n+1):
    for x in range(1,m+1):
        dap=max(dap,dp[y][x])
print(dap)
        