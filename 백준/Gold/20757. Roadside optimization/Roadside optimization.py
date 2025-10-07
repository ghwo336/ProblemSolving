t=int(input())
for _ in range(t):
    n=int(input())
    parents=[x for x in range(n)]
    def find(x):
        if parents[x]==x:
            return x
        parents[x]=find(parents[x])
        return parents[x]
    def union(x,y):
        px=find(x)
        py=find(y)
        parents[max(px,py)]=min(px,py)
    for i in range(n):
        li=list(map(int,input().split()))
        for j in range(len(li)):
            if i<j and li[j]==1:
                union(i,j)
    for i in range(n):
        find(i)
    di=dict()
    for x in parents:
        if x not in di:
            di[x]=1
        else:
            di[x]+=1
    dap=0
    for x in di:
        dap+=(di[x]-1)
    print(dap)
            
        
        