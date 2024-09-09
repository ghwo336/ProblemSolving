dp=[[0 for _ in range(10)] for _ in range(10)]
fiv=0
fivdp=[0]
for  x in range(1,10):
    fiv+=x*9*10**(x-1)
    fivdp.append(fiv)
    clone=0
    for y in range(1,10):
        dp[x][y]=dp[x-1][y]*10+10**(x-1)
        clone+=dp[x][y]
    dp[x][0]=fiv-clone

N=int(input())
strN=str(N)
totalNum=fivdp[len(strN)-1]+(N-10**(len(strN)-1)+1)*len(strN)
want=[0 for _ in range(10)]


l=len(strN)
for x in range(l-1):
    for y in range(1,10):
        want[y]+=(dp[l-x-1][y])*(int(strN[x]))
    want[int(strN[x])]+=(int(strN[x+1:])+1)
    for y in range(1,int(strN[x])):
        want[y]+=10**(l-x-1)
for x in range(1,int(strN[-1])+1):
    want[x]+=1

want[0]+=totalNum-sum(want)
print(*want)