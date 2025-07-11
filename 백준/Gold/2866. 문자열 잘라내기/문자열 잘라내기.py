import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]
for x in range(n):
    a=list(input())
    graph.append(a)

dap=0

start=1
end=n-1
while start<=end:
    mid=(start+end)//2
    s=set()
    pandan=0
    for y in range(m):
        a=''
        for z in range(mid,n):
            a+=graph[z][y]
        if a not in s:
            s.add(a)
        else:
            pandan=1
            break
    if pandan:
        start=start
        end=mid-1
    else:
        start=mid+1
        end=end
        dap=mid
    
print(dap)

    
    
        
    
    