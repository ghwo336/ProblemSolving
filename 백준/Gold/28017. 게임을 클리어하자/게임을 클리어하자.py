n,m=map(int,input().split())
games=[]
dp=[[5000000001 for _ in range(m)] for _ in range(n)]
for x in range(n):
    games.append(list(map(int,input().split())))

for x in range(m):
    dp[0][x]=games[0][x]
for x in range(1,n):
    for y in range(m):
        for z in range(m):
            if y!=z:
                dp[x][y]=min(dp[x][y],dp[x-1][z]+games[x][y])
print(min(dp[-1]))