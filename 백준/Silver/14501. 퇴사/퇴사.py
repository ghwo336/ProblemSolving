n=int(input())
dp=[0 for _ in range(n+1)]
li=[]
for x in range(n):
    a=list(map(int,input().split()))
    li.append(a)

for x in range(n):
    t=x+li[x][0]
    if t<n+1:
        for y in range(t,n+1):
            dp[y]=max(dp[y],dp[x]+li[x][1])
print(max(dp))
