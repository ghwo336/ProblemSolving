n,m=map(int,input().split())
li=list(map(int,input().split()))
li2=[]
for x in range(m-1):
    for y in range(x+1,m):
        li2.append(li[x]+li[y])
for x in li2:
    li.append(x)
li=list(set(li))
inf=100000001
dp=[inf for _ in range(n+1)]
dp[0]=0
li.sort()
for x in li:
    for y in range(x,n+1):
        if dp[y-x]!=inf:
            dp[y]=min(dp[y-x]+1,dp[y])
if dp[-1]!=inf:
    print(dp[-1])
else:
    print(-1)
