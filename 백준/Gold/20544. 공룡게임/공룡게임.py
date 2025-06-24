mod=1000000007
dp=[[0,0,0],[1,0,0],[1,1,1],[3,3,2]]
dp2=[[0,0],[1,0],[1,1],[2,2],[4,3]]
for x in range(1000):
    li=[0,0,0]
    li[0]=sum(dp[-1])%mod
    li[1]=(dp[-1][0]+(dp[-2][0]*2))%mod
    li[2]=(dp[-1][0]+dp[-2][0])%mod
    dp.append(li)
for x in range(1000):
    li=[0,0]
    li[0]=sum(dp2[-1])%mod
    li[1]=(dp2[-1][0]+dp2[-2][0])%mod
    dp2.append(li)
n=int(input())

print((sum(dp[n])-sum(dp2[n]))%mod)

