n=int(input())
li=list(map(int,input().split()))
li.sort()
dap=0
if len(li)==1:
    dap=li[0]
else:
    while li[-2]!=0:
        dap+=li[-2]
        li[-1]-=li[-2]
        li[-2]=0
        li.sort()
        
    dap+=li[-1]
if dap>1440:
    print(-1)
else:
    print(dap)