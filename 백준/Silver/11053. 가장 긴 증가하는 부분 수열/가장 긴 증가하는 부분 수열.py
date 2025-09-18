n=int(input())
li=list(map(int,input().split()))
dp=[1 for _ in range(n)]
for x in range(1,n):
    for y in range(x):
        if li[x]>li[y]:
            dp[x]=max(dp[y]+1,dp[x])
print(max(dp))
    