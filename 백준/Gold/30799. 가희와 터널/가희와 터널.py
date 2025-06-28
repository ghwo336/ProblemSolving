n=int(input())
mod=998244353
dp=[[0 for _ in range(8)] for _ in range(n+1)]
dp[1][0]=6
dp[0][0]=1


for i in range(1,n+1):
    for j in range(8):
        if j<=i:
            if j==0:
                dp[i][j]=6*dp[i-1][j]%mod
            elif j!=7:
                dp[i][j]=(6*dp[i-1][j]%mod+dp[i-1][j-1]%mod)%mod
            else:
                dp[i][j]=(7*dp[i-1][j]%mod+dp[i-1][j-1]%mod)%mod
        dp[i][j]%=mod
print(dp[-1][-1]%mod)


        