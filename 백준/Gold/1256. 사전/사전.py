n,m,k=map(int,input().split())
dp=[[1 for _ in range(m+1)] for _ in range(n+1)]
for x in range(1,n+1):
    for y in range(1,m+1):
        dp[x][y]=dp[x-1][y]+dp[x][y-1]

if dp[n][m]<k:
    print(-1)
else:
    dap=""
    while True:
        if n==0 or m==0:
            dap+="a"*n
            dap+="z"*m
            break
        if dp[n-1][m]>=k:
            dap+="a"
            n-=1
        else:
            dap+="z"
            k-=dp[n-1][m]
            m-=1
    print(dap)