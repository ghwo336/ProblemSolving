n,m=map(int,input().split())
graph=[[0 for _ in range(m+1)]]
for x in range(n):
    a=[0]+list(map(int,input().split()))
    graph.append(a)
for y in range(1,n+1):
    for x in range(1,m+1):
        graph[y][x]+=(graph[y-1][x]+graph[y][x-1]-graph[y-1][x-1])
k=int(input())
for _ in range(k):
    i,j,x,y=map(int,input().split())
    print(graph[x][y]-graph[i-1][y]-graph[x][j-1]+graph[i-1][j-1])