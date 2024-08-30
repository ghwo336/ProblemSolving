dp=[[1,0]]
for x in range(45):
    A=dp[-1][0]
    B=dp[-1][1]
    newA=B
    newB=B+A
    dp.append([newA,newB])
N=int(input())
print(*dp[N])