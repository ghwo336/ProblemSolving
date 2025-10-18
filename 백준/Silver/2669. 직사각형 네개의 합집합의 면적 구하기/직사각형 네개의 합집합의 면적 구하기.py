li=[[0 for _ in range(101)] for _ in range(101)]
for _ in range(4):
    a,b,c,d=map(int,input().split())
    for x in range(a,c):
        for y in range(b,d):
            li[x][y]=1
dap=0
for x in range(101):
    for y in range(101):
        dap+=li[x][y]
print(dap)