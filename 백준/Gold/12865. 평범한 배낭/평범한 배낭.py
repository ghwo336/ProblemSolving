n,k=map(int,input().split())
bag=[[0,0]]
for x in range(n):
    w,v=map(int,input().split())
    bag.append([w,v])
dp=[[0 for _ in  range(k+1)] for _ in range(n+1)]

for x in range(1,n+1):
    w=bag[x][0]
    v=bag[x][1]
    for y in range(1,k+1):
        if y>=w:
            dp[x][y]=max(dp[x-1][y-w]+v,dp[x-1][y])
        else:
            dp[x][y]=dp[x-1][y]
print(dp[-1][-1])
        

        
        