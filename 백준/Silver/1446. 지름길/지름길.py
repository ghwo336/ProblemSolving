n,d=map(int,input().split())
route=[]
for x in range(n):
    start,end,distance=map(int,input().split())
    route.append([end,start,distance])
route.sort()
dp=[x for x in range(d+1)]
for x in route:
    for y in range(x[0],d+1):
        dp[y]=min(dp[y],dp[x[1]]+x[2]+y-x[0])
print(dp[-1])