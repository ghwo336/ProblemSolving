n=int(input())
now=int(input())
dap=now
fiv=1
for x in range(n):
    a,b=map(int,input().split())
    now=now-b+a
    dap=max(dap,now)
    if now<0:
        fiv=0
if fiv:
    print(dap)
else:
    print(0)