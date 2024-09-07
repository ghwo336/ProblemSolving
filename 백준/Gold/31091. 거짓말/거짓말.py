N=int(input())
li=list(map(int,input().split()))
dp=[0]*(N+1)
dp1=[0]*(N+1)
dp2=[0]*(N+1)
plus=[]
minus=[]
dapli=[]
for x in li:
    if x>0:
        plus.append(x)
    else:
        minus.append(x)
for x in plus:
    dp1[0]+=1
    dp1[-x]-=1
for x in range(1,N+1):
    dp1[x]+=dp1[x-1]
dp1.reverse()

for x in minus:
    dp2[0]+=1
    if -x+1<=N:
        dp2[-x+1]-=1
for x in range(1,N+1):
    dp2[x]+=dp2[x-1]
for x in range(N+1):
    dp[x]=N-(dp1[x]+dp2[x])
for x in range(N+1):
    if dp[x]==x:
        dapli.append(x)
print(len(dapli))
print(*dapli)