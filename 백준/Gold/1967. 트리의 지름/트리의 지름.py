import sys
sys.setrecursionlimit(10**5)
def dfs(now,before,value):
    global dap
    for x in graph[now]:
        if x[0]!=before:
            dap=max(dap,value+x[1])
            dfs(x[0],now,value+x[1])


n=int(input())
graph=[[] for _ in range(n+1)]
noLeaf=set()
for x in range(n-1):
    mom,sun,value=map(int,input().split())
    graph[mom].append((sun,value))
    graph[sun].append((mom,value))
    noLeaf.add(mom)
dap=0

for x in range(1,n+1):
    if x not in noLeaf:
        dfs(x,x,0)

print(dap)