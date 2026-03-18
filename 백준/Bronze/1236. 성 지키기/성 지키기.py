n,m=map(int,input().split())
graph=[]
for x in range(n):
    li=list(input())
    graph.append(li)
dap1=0
dap2=0
for x in range(n):
    fiv=1
    for y in range(m):
        if graph[x][y]=='X':
            fiv=0
    if fiv:
        dap1+=1
for y in range(m):
    fiv=1
    for x in range(n):
        if graph[x][y] == 'X':
            fiv=0
    if fiv:
        dap2+=1
print(max(dap1,dap2))