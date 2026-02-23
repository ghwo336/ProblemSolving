n,m=map(int,input().split())
dap=0
graph=[]
for x in range(n):
    li=list(input())
    graph.append(li)
for x in range(n):
    for y in range(m):
        if graph[x][y]=='0':
            dap+=1
print(min(dap,n*m-dap))