t=int(input())

dp=[[ x for x in range(15)] for _ in range(15)]

for x in range(1,15):
    for y in range(1,15):
        f=0
        for z in range(y+1):
            f+=dp[x-1][z]
        dp[x][y]=f
for _ in range(t):
    a=int(input())
    b=int(input())
    print(dp[a][b])
            
    