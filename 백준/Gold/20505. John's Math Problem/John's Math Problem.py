import sys
input=sys.stdin.readline
mod=998244353
num=input().strip()
def paw(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    fiv=(paw(a,b//2))%mod
    if b%2==1:
        return fiv*fiv*a%mod
    else:
        return fiv*fiv%mod
l=len(num)
dap=0
for x in range(l):
    now=paw(11,l-x-1)*paw(2,x)*(int(num[x]))%mod
    dap+=now
    dap%=mod
print(dap)
