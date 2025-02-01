n,s,m=map(int,input().split())
li=list(map(int,input().split()))
dp=[[False for _ in range(m+1)] for _ in range(n+1)]
dp[0][s]=True
for x in range(n):
    for y in range(m+1):
        if dp[x][y]==True:
            if 0<=y+li[x]<=m:
                dp[x+1][y+li[x]]=True
            if 0<=y-li[x]<=m:
                dp[x+1][y-li[x]]=True


fiv=-1

for x in range(m+1):
    if dp[-1][x]:
        fiv=x
print(fiv)