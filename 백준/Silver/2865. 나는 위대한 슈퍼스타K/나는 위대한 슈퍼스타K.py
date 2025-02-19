n,m,k=map(int,input().split())
dp=[0 for _ in range(n)]
for x in range(m):
    li=list(input().split())
    for y in range(0,len(li),2):
        dp[int(li[y])-1]=max(dp[int(li[y])-1],float(li[y+1]))

dp.sort(reverse=True)
dap=0
for x in range(k):
    dap+=dp[x]
print(round(dap,2))
        
        