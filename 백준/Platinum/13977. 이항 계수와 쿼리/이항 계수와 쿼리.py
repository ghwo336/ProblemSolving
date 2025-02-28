def pow(x,n):
    global mod
    if n==1:
        return x%mod
    t=pow(x,n//2)
    if n%2==0:
        return t*t%mod
    else:
        return t*t*x%mod

m=int(input())
mod=1000000007
dp=[1 for _ in range(4000001)]
for x in range(2,4000001):
    dp[x]=(dp[x-1]*x)%mod

for x in range(m):
    n,k=map(int,input().split())
    print(dp[n]*pow(dp[k]*dp[n-k]%mod,mod-2)%mod)
