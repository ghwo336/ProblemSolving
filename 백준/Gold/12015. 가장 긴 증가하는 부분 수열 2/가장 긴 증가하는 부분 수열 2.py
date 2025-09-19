import sys
input=sys.stdin.readline
def binary(start,end,target):
    if start>end:
        dp[start]=target
        return
    mid=(start+end)//2
    if dp[mid]>=target:
        return binary(0,mid-1,target)
    else:
        return binary(mid+1,end,target)

n=int(input())
li=list(map(int,input().split()))
dp=[0]
for x in range(n):
    if dp[-1]<li[x]:
        dp.append(li[x])
    else:
        binary(0,len(dp)-1,li[x])
print(len(dp)-1)