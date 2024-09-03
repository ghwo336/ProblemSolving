n,m=map(int,input().split())
dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
for x in range(1,m+1):
    day,page=map(int,input().split())
    for y in range(n+1):
        if y>=day and dp[x][y]<dp[x-1][y-day]+page :
            dp[x][y]=max(dp[x][y],dp[x-1][y-day]+page,dp[x][y-1],dp[x-1][y])
        else:
            dp[x][y]=max(dp[x][y],dp[x-1][y],dp[x][y-1],dp[x-1][y])



print(dp[-1][-1])