dp=[0,0,1]
for x in range(3,11):
    if x%2==0:
        dp.append((x//2)**2+dp[x//2]+dp[x//2])
    else:
        dp.append((x//2)*(x//2+1)+dp[x//2]+dp[x//2+1])
N=int(input())
print(dp[N])