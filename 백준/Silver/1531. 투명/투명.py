n,m=map(int,input().split())
li=[[0 for _ in range(101)] for _ in range(101)]
for x in range(n):
    a,b,c,d=map(int,input().split())
    for x in range(a,c+1):
        for y in range(b,d+1):
            li[x][y]+=1
dap=0
for x in range(1,101):
    for y in range(1,101):
        if li[x][y]>m:
            dap+=1
print(dap)