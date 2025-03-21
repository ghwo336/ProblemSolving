import sys
input=sys.stdin.readline
s=set()
s=[True]*100000
p,k=map(int,input().split())
n=p
l=len(str(n))
pow=10**l%k

dap=0
pandan=1
while True:
    dap+=1
    if n%k==0:
        break
    else:
        if s[n%k]:
            s[n%k]=False
            n=(n*pow+p)%k            
        else:
            pandan=0
            break
if pandan:
    print(dap)
else:
    print(-1)
            
        