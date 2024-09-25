N=int(input())
M=int(input())
li=[]

for x in range(M):
    a=int(input())
    li.append(a)
dp=[1,1]
for x in range(41):
    dp.append(dp[-1]+dp[-2])
if not li:
    print(dp[N])
else:
    dap=dp[li[0]-1]
    dap*=dp[N-li[-1]]
    if len(li)>=2:
        for x in range(1,len(li)):
            dap*=(dp[li[x]-li[x-1]-1])
    print(dap)