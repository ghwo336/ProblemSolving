def sol():
    n=int(input())
    coins=list(map(int,input().split()))
    m=int(input())
    dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
    for x in range(1,n+1):
        coin=coins[x-1]
        for y in range(m+1):
            if y>coin:
                dp[x][y]=dp[x-1][y]+dp[x][y-coin]
            elif y==coin:
                dp[x][y]=dp[x-1][y]+1
            else:
                dp[x][y]=dp[x-1][y]
    print(dp[-1][-1])


t=int(input())
for i in range(t):
    sol()
        
        